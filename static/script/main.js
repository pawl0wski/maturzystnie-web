
class ResponsiveNavBar{
    constructor(){
        this.navbar = $("nav")
        this.navbarBtn = $("nav img#responsive-button")
        this.navbarMenu = $("div.nav-menu")
        this.navbarShowed = false;
        this.connectButton();
    }

    connectButton(){
        let thisObj = this
        this.navbarBtn.click(() => {
            this.onNavbarBtnClick.call(thisObj);
        });
        $("div.nav-menu a.nav-link").click(() => {
            this.onNavbarBtnClick.call(thisObj);
        });
    }

    onNavbarBtnClick(action){
        if (this.navbarShowed) {
            this.navbarBtn.attr("src", "/static/img/responsive-btn.png");
            this.navbarMenu.animate({top: "-100%"}, "fast", () => {
                this.navbarMenu.css("display", "none")
            })
            this.navbarShowed = false;
        }else{
            this.navbarBtn.attr("src", "/static/img/close.png");
            this.navbarMenu.css("display", "flex")
            this.navbarMenu.animate({top: "0%"}, "fast")
            this.navbarShowed = true;
        }
    }
}

(() => {
    let rn = new ResponsiveNavBar()
})()