if status is-interactive
end

function fish_prompt
	set_color green
	echo -n (whoami)

	set_color normal
	echo -n " in "

	set_color blue
	echo -n (prompt_pwd)

	set_color normal
	echo -n ' $ '
end


alias rebuild = "sudo nixos-rebuild switch --flake ~/nix#sam"
funcsace rebuild
