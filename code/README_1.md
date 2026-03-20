
```html
<!DOCTYPE html>
<html>
<head>
    <title>Iris AR Viewer</title>

    <!-- Model Viewer -->
    <script type="module"
        src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js">
    </script>

    <style>
        body {
            margin: 0;
            text-align: center;
            font-family: Arial;
        }

        model-viewer {
            width: 100%;
            height: 90vh;
        }
    </style>
</head>
<body>

<h2>🌸 Iris AR Model</h2>

<model-viewer 
    src="/static/models/Iris.glb"
    ar
    auto-rotate
    camera-controls
    shadow-intensity="1"
    style="background-color: #f5f5f5; width: 100%; height: 80vh;"
    camera-orbit="0deg 75deg 2m"
    scale="0.289 0.333 0.5" 
    alt="A 3D model of an Iris">
</model-viewer>

<!-- Axis Info -->
<div>
    <p><b>X Axis → Virginica (VG)</b></p>
    <p><b>Y Axis → Setosa (IS)</b></p>
    <p><b>Z Axis → Versicolor (VC)</b></p>
</div>

</body>
</html>
```


