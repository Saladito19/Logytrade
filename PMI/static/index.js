const body = document.querySelector('body'),
    sidebar = body.querySelector('nav'),
    toggle = body.querySelector('.toggle'),
    modeswitch = body.querySelector('.toggle-switch'),
    modeText = body.querySelector('.mode-text');


toggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");

})

modeswitch.addEventListener("click", () => {
    body.classList.toggle("dark");
    if (body.classList.contains("dark")) {
        modeText.innerText = "ligth mode"

    } else {
        modeText.innerText = "Dark mode"
    }
})