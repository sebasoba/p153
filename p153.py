<html>
<head>
<script src="https://aframe.io/releases/0.6.0/aframe.min.js"> </script> 
</head>
<body>

AFRAME.registerComponent("base",{
    schema: {
        radius: { type: "number", default: 150 },
        height: { type: "number", default: 3 },
    },

    update: function() {
        window.addEventListener("click", e => {
            this.data.clickCounter = this.data.clickCounter + 1;
            if(this.data.clickCounter === 1) {
                const rotation = { x: 0, y: 20, z: 0 };
                this.el.setAttribute("rotation", rotation);
            } else if (this.data.clickCounter === 2)
            {
                const rotation = { x: 0, y: 20, z: 0 };
            }
        });
        
    }

    
})

<a-entity
    gltf-model="#scuba_driver"
    scale="0.1 0.1 0.1"
    position="5 0 15"
    rotation="0 90 -20"
    diver-rotation-reader

></a-entity>
</body>
</html>