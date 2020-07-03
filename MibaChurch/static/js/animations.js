window.onload = function () {

    var tlC = gsap.timeline({ repeat: -1 });
    tlC.from('.arrow', { duration: 1.8, delay: .5, opacity: 0, y: -15 })

    // gsap.registerPlugin(CSSRulePlugin);

    // var ruleOne = CSSRulePlugin.getRule("header::before");
    // var ruleTwo = CSSRulePlugin.getRule("header::after");

    var tl = gsap.timeline({});
    // tl.to('.overlay-one', { duration: .5, x: -1400 })
    // tl.to('.overlay-two', { duration: .5, x: -1400 }, "-=.3")
    // tl.to('.overlay-three', { duration: .5, x: -1400 }, "-=.3")
    tl.from('.nav-container', { duration: 1, opacity: 0, y: -10, ease: "bounce.out" })
    tl.from('.hero-content h1', { duration: 1, opacity: 0, y: -15, ease: "expo.out" })
    tl.from('.hero-content span', { duration: 1, opacity: 0, x: -30, ease: "back.out(1.7)", }, "-=.5")
    tl.from('.hero-content a', { duration: 1, opacity: 0, y: 15, ease: "back.out(1.7)", }, "-=.5")
}