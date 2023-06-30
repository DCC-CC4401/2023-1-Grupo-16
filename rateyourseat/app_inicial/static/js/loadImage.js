<script>
    function previewImages() {
        var preview = document.getElementById("image-preview");
        var files = document.getElementById("image-input").files;

        preview.innerHTML = ""; // Clear previous preview

        for (var i = 0; i < files.length; i++) {
            var file = files[i];
            var reader = new FileReader();

            reader.onload = function (event) {
                var image = document.createElement("img");
                image.src = event.target.result;
                image.style.maxWidth = "200px";
                image.style.maxHeight = "200px";
                preview.appendChild(image);
            };

            reader.readAsDataURL(file);
        }
    }

    var imageInput = document.getElementById("image-input");
    imageInput.addEventListener("change", preview



