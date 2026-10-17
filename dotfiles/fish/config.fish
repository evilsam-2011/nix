if status is-interactive
end

set -g fish_prompt_pwd_dir_length 0

function fish_prompt
    set_color green
    printf '[%s@%s:%s]$ ' (whoami) (hostname -s) (prompt_pwd)
    set_color normal
end


zoxide init fish | source
alias rebuild="sudo nixos-rebuild switch --flake ~/nix#sam"
alias ls="eza --icons"
alias la="eza --icons --all"
alias ll="eza --icons --long"
alias lg="lazygit"
alias tmux="tmux -u"

