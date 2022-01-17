const programs: string[] = ['main', 'flle', 'fllc', 'ftc', 'frc'];

const section:HTMLElement = document.getElementById("main-program-navigation");
const program_logos = section.getElementsByClassName("program-nav-box");

for (let i = 0; i < program_logos.length; i++) {
    const logo = program_logos[i] as HTMLElement;
    if (logo.classList.contains("flld-brand")) {
        continue // no sub-menu for FLL Discover, so don't update anything if moused over
    }

    logo.addEventListener("mouseenter", function(e) {
        for (const prog of programs) {
            const menu = document.getElementById(prog + "-menu");
            if ((<Element>e.target).id.startsWith(prog)) {
                menu.classList.add("current-program");
            } else {
                menu.classList.remove("current-program");
            }
        }
    })
}
