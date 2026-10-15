{ config, pkgs, inputs, ... }:
{
  imports =
    [ # Include the results of the hardware scan.
      ./hardware-configuration.nix
    ];

  # Use the systemd-boot EFI boot loader.
  boot.loader.systemd-boot.enable = true;
  boot.loader.efi.canTouchEfiVariables = true;

  # Use latest kernel.
  boot.kernelPackages = pkgs.linuxPackages_latest;

  networking.hostName = "sam"; # Define your hostname.
  # networking.wireless.enable = true;  # Enables wireless support via wpa_supplicant.

  nix.settings.experimental-features = [ "nix-command" "flakes" ];

  # Configure network proxy if necessary
  # networking.proxy.default = "http://user:password@proxy:port/";
  # networking.proxy.noProxy = "127.0.0.1,localhost,internal.domain";

  # Enable networking
  networking.networkmanager.enable = true;

  # Set your time zone.
  time.timeZone = "Asia/Kolkata";

  virtualisation.podman.enable = true;

  services.xserver.windowManager.qtile = {
    enable = true;
    extraPackages = python3Packages: with python3Packages; [ qtile-extras ];
  };

  # Select internationalisation properties.
  i18n.defaultLocale = "en_IN";

  i18n.extraLocaleSettings = {
    LC_ADDRESS = "en_IN";
    LC_IDENTIFICATION = "en_IN";
    LC_MEASUREMENT = "en_IN";
    LC_MONETARY = "en_IN";
    LC_NAME = "en_IN";
    LC_NUMERIC = "en_IN";
    LC_PAPER = "en_IN";
    LC_TELEPHONE = "en_IN";
    LC_TIME = "en_IN";
  };

  # Configure keymap in X11
  services.xserver.xkb = {
    layout = "us";
    variant = "";
  };

  # Define a user account. Don't forget to set a password with ‘passwd’.
  users.users."sam" = {
    isNormalUser = true;
    description = "sam";
    extraGroups = [ "networkmanager" "wheel" ];
    packages = with pkgs; [];
  };
# window managers
  # Enable Plasma 
  services = {
    displayManager.ly.enable = true;
  };

  # Allow unfree packages
  nixpkgs.config.allowUnfree = true;

 environment.systemPackages = with pkgs; [
 vim
 git
 opencode
 waybar
 waypaper
 swaybg
 mako
 neovim
 librewolf
 fuzzel
 fish
 zoxide
 tmux
 foot
 tree
 emacs
 fastfetch
 ripgrep
 fd
 bat
 gcc
 gnumake
 tree-sitter
 obs-studio
 mpv
 fzf
 distrobox
 eza
 yazi

 ];

 programs.fish.enable = true;

 users.defaultUserShell = pkgs.fish; 


 hardware.graphics.extraPackages = with pkgs; [
  intel-media-driver
  intel-vaapi-driver
 ];

 xdg.portal = {
  enable = true;
  wlr.settings.screencast = {
    chooser_type = "none";
    output_name = "eDP-1";
  };
 };


 fonts.packages = with pkgs; [
  nerd-fonts.jetbrains-mono
  nerd-fonts.iosevka
  ];


  system.stateVersion = "26.05"; # Did you read the comment?

}
