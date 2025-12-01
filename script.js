async function runPython() {
    // Loads pyodide, then installs pillow
    if (!window.pyodide) {
        window.pyodide = await loadPyodide();
        await pyodide.loadPackage("micropip");
        await pyodide.runPythonAsync("import micropip; await micropip.install('pillow')");
    }

    // Importing file system
    let response = await fetch("skingenerator.py");
    let code = await response.text();
    pyodide.FS.writeFile("skingenerator.py", code);

    let templates = ['base0', 'hair0', 'hair1', 'eye0', 'eye1', 'eye2']

    try {
        pyodide.FS.mkdir("assets");
    } catch (e) {
        // Directory already exists, ignore
    }

    for (let name of templates) {
        let response = await fetch(`assets/${name}.png`);
        let buffer = await response.arrayBuffer();
        pyodide.FS.writeFile(`assets/${name}.png`, new Uint8Array(buffer));
        let maskResponse = await fetch(`assets/${name}_mask.png`);
        if (maskResponse.ok) {
            let maskBuffer = await maskResponse.arrayBuffer();
            pyodide.FS.writeFile(`assets/${name}_mask.png`, new Uint8Array(maskBuffer));
        }
    }

    // Generates base64 encoded skin
    let base64 = await pyodide.runPythonAsync(`
            from PIL import Image
            import random, io, base64
            import skingenerator

            img = skingenerator.randomSkin()

            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            base64_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
            base64_str
            `);

    document.getElementById("myImage").src = "data:image/png;base64," + base64;
    document.getElementById("myImage").style.visibility = "visible";
}