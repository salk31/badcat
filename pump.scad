$fn = 180;

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

c = 0.1;
c2 = 2 * c;

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
module motor2() {
    translate([0, 0, mot_bump_l + 0.2]) motor();
}

module blades() {
    cylinder(h = 1, d = imp_d);
    t = 0.8;
    for (a = [0:60:359]) 
        rotate(a)
            translate([-t / 2, 0, 0])
                cube([t, imp_d / 2, imp_l]);
    
}

module imp() {
    translate([0, 0, -imp_shaft_l]) rotate([180, 0, 0]) blades();
    
    rotate([180, 0, 0])
        cylinder(h = imp_shaft_l, d = imp_shaft_d);
}

module imp_r() {
    // clearance for main rotor
    translate([0, 0, -imp_shaft_l + c])
        rotate([180, 0, 0]) 
            cylinder(h = imp_l + c, d = imp_d + c2);
    
    // inlet
    translate([0, 0, -imp_shaft_l + c])
        rotate([180, 0, 0]) 
            cylinder(h = 2 * imp_l + c, d = 0.5 * imp_d );
    
    rotate([180, 0, 0])
        cylinder(h = imp_shaft_l + c2, d = imp_shaft_d + c2);
}

module body() {
    difference() {
        translate([0, 0, -1 + mot_l - body_l]) cube_cxy([body_d, body_d, body_l]);
        imp_r(); 
        motor2();
    }
}

module foo() {
    translate([-10, 0, -40]) cube([20, 40, 80]);
}

//intersection() {foo(); body();} // back
difference() {body(); foo(); translate([4, 0, -23]) rotate([90, 0, 0]) cylinder(h = 20, r = 1.8);} // front
difference() {imp(); motor2();}
//blades();
