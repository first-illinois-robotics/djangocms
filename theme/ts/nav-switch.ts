let programs: string[] = ['flle', 'fllc', 'ftc', 'frc'];

let section:HTMLElement = document.getElementById("main-program-navigation");
const program_logos = section.getElementsByClassName("program-nav-box");
for (let i = 0; i < program_logos.length; i++) {
    const logo = program_logos[i] as HTMLElement;
    logo.addEventListener("mouseenter", function(e) {
        for (let prog of programs) {
            const menu = document.getElementById(prog + "-menu");
            if ((<Element>e.target).id.startsWith(prog)) {
                menu.style.display = "block";
            } else {
                menu.style.display = "none";
            }
        }
    })
}
