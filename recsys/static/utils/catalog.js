document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.catalog-navbar button');
    const contentBlocks = document.querySelectorAll('.content-block');
    const activebuttons = document.querySelectorAll('.product-button');

    function switchContent(targetId) {
        contentBlocks.forEach(block => block.classList.remove('active'));

        const targetBlock = document.querySelector(`${targetId}`);
        if (targetBlock) {
            targetBlock.classList.add('active');
        }
    }

    buttons.forEach(button => {
        button.addEventListener('click', function(event) {
            let targetId = button.getAttribute('data-target');
            switchContent(targetId);
        });
    });

    activebuttons.forEach(button => {
        button.addEventListener('click', () => {
            activebuttons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
        });
    });
});
