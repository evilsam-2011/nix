{ config, pkgs, ... }:
{
  home.username = "sam";
  home.homeDirectory = "/home/sam";
  home.stateVersion = "26.11";

  programs.bash = {
    enable = true;
    shellAliases = {
      btw = "echo i use nixos btw";
      rebuild = "sudo nixos-rebuild switch --flake ~/nix#sam";
      vim = "nvim";
      edit = "sudo vim ~/nix/";
    };
  };

  home.file = {
    ".config/waybar" = {
      source = ./dotfiles/waybar;
      recursive = true;
    };
    ".config/foot" = {
    source = ./dotfiles/foot;
    recursive = true;
    };
    ".config/sway" = {
    source = ./dotfiles/sway;
    recursive = true;
    };
    ".config/fuzzel" = {
    source = ./dotfiles/fuzzel;
    recursive = true;
    };
    ".config/fish" = {
    source = ./dotfiles/fish;
    recursive = true;
    };
    ".config/nvim" = {
    source = ./dotfiles/nvim;
    recursive = true;
    };
  };
}
