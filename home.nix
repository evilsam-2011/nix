{ config, pkgs, ... }:
{
  home.username = "sam";
  home.homeDirectory = "/home/sam";
  home.stateVersion = "26.11";

  programs.bash = {
    enable = true;
    shellAliases = {
      btw = "echo i use nixos btw";
      rebuild = "sudo nixos-rebuild switch";
      vim = "nvim";
      edit = "sudo vim /etc/nixos/";
    };
  };

  programs.kitty = {
    enable = true;
    settings = {
      confirm_os_window_close = 0;
      background_opacity = 0.7;
    };
  };
}
