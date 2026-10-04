 { config, pkgs, ...}:

 {
    home.username = "sam";
    home.homeDirectory = "/home/tony";
    home.stateVersion = "26.11";
    programs.bash = {
	enable = true;
	shellAliases = {
	    btw = "echo i use nixos btw";		
	};
    };	
 }

