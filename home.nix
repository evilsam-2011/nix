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

  home.file = {
    ".config/waybar" = {
      source = ./dotfiles/waybar;
      recursive = true;
    };
  };
}
