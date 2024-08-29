document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    var formData = new FormData();
    var files = document.getElementById('files').files;
    
    for (var i = 0; i < files.length; i++) {
        formData.append('files[]', files[i]);
    }
    
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            return response.blob();
        } else {
            document.getElementById('message').textContent = "Failed to convert images!";
            throw new Error('Failed to convert images');
        }
    })
    .then(blob => {
        var url = window.URL.createObjectURL(blob);
        var a = document.createElement('a');
        a.href = url;
        a.download = 'output.pdf';
        document.body.appendChild(a);
        a.click();
        a.remove();
        document.getElementById('message').textContent = "PDF created successfully!";
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
