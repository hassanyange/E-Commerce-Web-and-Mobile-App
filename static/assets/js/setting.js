document.getElementById('profilePictureInput').addEventListener('change', function() {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(event) {
            document.getElementById('profileImage').setAttribute('src', event.target.result);
        };
        reader.readAsDataURL(file);
    }
});

document.getElementById('settingsForm').addEventListener('submit', function(event) {
    event.preventDefault();
    // Here you can handle the form submission, e.g., send the data to the server
    alert('Settings saved successfully!');
});
