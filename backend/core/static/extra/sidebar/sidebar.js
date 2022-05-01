var sidebar = document.getElementById("sideBar")
function manipularNav() {
    if (sidebar.classList.contains("fechado")) {
        sidebar.classList.add("aberto");
        sidebar.classList.remove("fechado");
        document.getElementById("botaoSideBar").style.marginLeft = "125px";
        document.getElementById("sideBar").style.width = "180px";
        document.getElementById("conteudo_sidebar").style.marginLeft = "180px";
    } else if (sidebar.classList.contains("aberto")) {
        sidebar.classList.add("fechado");
        sidebar.classList.remove("aberto");
        document.getElementById("botaoSideBar").style.marginLeft = "0";
        document.getElementById("sideBar").style.width = "0";
        document.getElementById("conteudo_sidebar").style.marginLeft = "10px";
    }
}