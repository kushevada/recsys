document.addEventListener('DOMContentLoaded', function() {
    const toggleFormsButton = document.getElementById('toggleFormsButton');
    const formsContainers = document.querySelectorAll('.forms-container');

    toggleFormsButton.addEventListener('click', function() {
        formsContainers.forEach(container => {
            if (container.style.display === 'none') {
                container.style.display = 'inline-block';
            } else {
                container.style.display = 'none';
            }
        });
    });
});