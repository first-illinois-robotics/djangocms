
const donateProgramSelect:HTMLSelectElement = <HTMLSelectElement>document.getElementById("donateProgramSelect");
const donateBusiness: HTMLInputElement = <HTMLInputElement>document.getElementById("donateBusiness");

donateProgramSelect.addEventListener("change", function(_) {
    if (donateProgramSelect.value == "FLL Program") {
        donateBusiness.value = "fllillinois@yahoo.com"
    } else {
        donateBusiness.value = "contact@ilftc.org"
    }
})