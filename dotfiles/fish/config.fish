if status is-interactive
end

set -g fish_prompt_pwd_dir_length 0

function fish_prompt
    # Set color to blue
    set_color blue

    # Print [username@path] $
    printf '[%s@%s] $ ' (whoami) (prompt_pwd)

    # Reset color back to normal
    set_color normal
end


zoxide init fish | source
alias rebuild="sudo nixos-rebuild switch --flake ~/nix#sam"
alias ls="eza --icons" 
