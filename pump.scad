$fn = 180;

mot_l = 20.2;
mot_d = 8.7; // 8.6 too tight for simpler version

mot_shaft_l = 5; // measure from face of motor
mot_shaft_d = 1.2; // actually 1.0 but 1.1 too tight, 1.3 too loose

mot_bump_l = 0.6;
mot_bump_d = 2.5;

imp_l = 5;
imp_d = 20;



c = 0.1;
c2 = 2 * c;
cp = 0.5;
cp2 = 2 * cp;



module cube_cxy(d) {
    translate([-d.x / 2, -d.y / 2, 0]) cube(d);
}

module motor(shaft_x = 1) {
    cylinder(h = mot_l, d = mot_d);
    rotate([180, 0, 0]) cylinder(h = shaft_x * mot_shaft_l, d = mot_shaft_d);
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
    //translate([0, 0, -imp_shaft_l + c])
    //    rotate([180, 0, 0]) 
    //        #cylinder(h = 2 * imp_l + c, d = 0.5 * imp_d );

    
    // outlet
    outlet_d = imp_l + cp2;
    translate([0, -imp_d / 2 + outlet_d / 2,   imp_l / 2 ]) rotate([0, 90, 0]) cylinder(h = 20, d = outlet_d);
}

module imp_p() motor_p() translate([0, 0, -1]) rotate([0, 180, 45]) children();

module body() {
    difference() {
        #motor_p() translate([0, 0, -6 -cp]) cylinder(r = 12, h = 20);
        imp_p() imp_r();
        motor_p() motor();
    }
}


module pump_p() {
    translate([0, 0, 14]) rotate([0, -45, 0]) children();
}

module base() {
    or = 40;
    h = 10;
    w = 1;
    difference() {
        union() {
            difference() {
                cylinder(r = or, h = h);
                translate([0, 0, w]) cylinder(r = or - w, h = h - w);
            }
            translate([0, 0, 0]) cube_cxy([20, 20, 10]);
        }
        // TODO remove pump
        pump_p() hull() body();
        #pump_p() imp_p() imp_r();
    }
}


//body();

//difference() {imp_p() imp(); motor_p() motor(2);};
//motor_p() motor();
base();
//pump_p() body();

// print 5
// - motor shaft too loose, must have been elephants foot last time
// - motor fits very nicely
// - maybe not enough clearance for "face" of impeller?

// print 4 - simpler design
// - motor doesn't fit, just slightly too tight
// - shaft doesn't fit
// - imp spins nicely straight from printer (first time)
// - printing body (imp up) is crap without support

// print 3
// - printing on raft much better but lost bit of one blade
// - trying running it but imp got stuck and shaft melted and then too big too fit
// - basically, shaft a pain, printing in two halves causes alignment problems

// print 2
// - hole for motor shaft still too small
// - printing imp without adhesion didn't work but annoying to remove with

// print 1
// - motor bit snug
// - impeller elephants foot means hard to fit and water intake blocked
// - motor shaft too tight
// - don't print with supports!