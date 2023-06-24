$fn = 180;

mot_l = 20.2;
mot_d = 8.6;

mot_shaft_l = 5; // measure from face of motor
mot_shaft_d = 1.2; // actually 1.0 but 1.1 too tight

mot_bump_l = 0.6;
mot_bump_d = 2.5;

imp_l = 5;
imp_d = 20;

imp_shaft_l = 20;
imp_shaft_d = 3;

c = 0.1;
c2 = 2 * c;
cp = 0.5;
cp2 = 2 * cp;

wall = 2;
wall2 = 2 * wall;
body_l = mot_l + imp_shaft_l + imp_l;
body_d = imp_d + wall2;

module cube_cxy(d) {
    translate([-d.x / 2, -d.y / 2, 0]) cube(d);
}

module motor() {
    cylinder(h = mot_l, d = mot_d);
    rotate([180, 0, 0]) cylinder(h = mot_shaft_l, d = mot_shaft_d);
    rotate([180, 0, 0]) cylinder(h = mot_bump_l, d = mot_bump_d);
    
    // clearance for cables
    cylinder(h = mot_l + 10, d = mot_d - 2);
}

// motor with usable start of shaft at z = 0
module motor_p() {
    translate([0, 0, mot_bump_l + 0.2]) rotate([0, 90, 0]) children();
}

module imp() {
    cylinder(h = 1, d = imp_d);
    cylinder(h = imp_l, d = 3); // extra for shaft
    t = 0.8;
    for (a = [0:60:359]) 
        rotate(a)
            translate([-t / 2, 0, 0])
                cube([t, imp_d / 2, imp_l]);
}

module imp_r() {
    // clearance for main rotor
    translate([0, 0, -cp])
        //rotate([180, 0, 0]) 
            cylinder(h = imp_l + cp2, d = imp_d + cp2);
    
    // inlet
    translate([0, 0, -imp_shaft_l + c])
        rotate([180, 0, 0]) 
            #cylinder(h = 2 * imp_l + c, d = 0.5 * imp_d );

    
    // outlet
    outlet_d = imp_l + cp2;
    translate([0, -imp_d / 2 + outlet_d / 2,   imp_l / 2 ]) rotate([0, 90, 0]) cylinder(h = 20, d = outlet_d);
}

module imp_p() motor_p() translate([0, 0, -1]) rotate([0, 180, 45]) children();

module body() {
    difference() {
        #motor_p() translate([0, 0, -6]) cylinder(r = 12, h = 20);
        imp_p() imp_r();
        motor_p() motor();
    }
}


body();

difference() {imp_p() imp(); motor_p() motor();};
//imp_p() imp_r();