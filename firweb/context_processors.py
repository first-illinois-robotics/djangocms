from django.http import HttpRequest


def program(request: HttpRequest):
    program_info = {
        "home": {
            "internal_name": "home",
            "desktop_img": "horizontal-4c.png",
            "mobile_img": "horizontal-4c-reverse.png",
            "full_name": "FIRST Illinois Robotics",
            "extra_img_classes": "brand-logo",
            "url": "home"
        },
        "flld": {
            "internal_name": "flld",
            "desktop_img": "FLL-RGB_Discover-vert-one-color-reverse.png",
            "mobile_img": "FLL-RGB_Discover-horiz-one-color-reverse.png",
            "full_name": "FIRST LEGO League Discover",
            "extra_img_classes": "fll-logo",
            "url": "fll-discover"
        },
        "flle": {
            "internal_name": "flle",
            "desktop_img": "FLL-RGB_Explore-vert-one-color-reverse.png",
            "mobile_img": "FLL-RGB_Explore-horiz-one-color-reverse.png",
            "full_name": "FIRST LEGO League Explore",
            "extra_img_classes": "fll-logo",
            "url": "fll-explore"
        },
        "fllc": {
            "internal_name": "fllc",
            "desktop_img": "FLL-RGB_Challenge-vert-one-color-reverse.png",
            "mobile_img": "FLL-RGB_Challenge-horiz-one-color-reverse.png",
            "full_name": "FIRST LEGO League Challenge",
            "extra_img_classes": "fll-logo",
            "url": "fll-challenge"
        },
        "ftc": {
            "internal_name": "ftc",
            "desktop_img": "FIRSTTech_Type_White.png",
            "mobile_img": "FIRSTTech_iconHorz_OneColor_reverse.svg",
            "full_name": "FIRST Tech Challenge",
            "extra_img_classes": "non-fll-logo",
            "url": "ftc"
        },
        "frc": {
            "internal_name": "frc",
            "desktop_img": "FIRSTRobotics_Type_White.png",
            "mobile_img": "FIRSTRobotics_iconHorz_OneColor_reverse.svg",
            "full_name": "FIRST Robotics Competition",
            "extra_img_classes": "non-fll-logo",
            "url": "frc"
        },
    }

    current_program = None
    for program in program_info.keys():
        if request.path.startswith("/" + program_info[program]["url"]):
            current_program = program
            program_info[program]["current"] = True
        else:
            program_info[program]["current"] = False

    if current_program is None:
        program_info["home"]["current"] = True

    return {
        "programs": program_info,
        "program": current_program
    }


