mot_l = 20.2;
mot_d = 8.5;

mot_shaft_l = 5; // measure from face of motor
mot_shaft_d = 1;

mot_bump_l = 0.6;
mot_bump_d = 2.5;

imp_l = 5;
imp_d = 10;

imp_shaft_l = 20;
imp_shaft_d = 3;



module motor() {
    cylinder(h = mot_l, d = mot_d);
    rotate([180, 0, 0]) cylinder(h = mot_shaft_l, d = mot_shaft_d);
    rotate([180, 0, 0]) cylinder(h = mot_bump_l, d = mot_bump_d);
    
    // clearance for cables
    cylinder(h = mot_l + 10, d = mot_d - 2);
}

module shaft() {
    rotate([180, 0, 0]) cylinder(h = imp_shaft_l, d = imp_shaft_d);
}

module imp() {
    rotate([180, 0, 0]) cylinder(h = imp_l, d = imp_d);
}


translate([0, 0, mot_bump_l + 0.2]) motor();
shaft();
translate([0, 0, -imp_shaft_l]) imp();