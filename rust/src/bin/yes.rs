use std::env;
use std::process::ExitCode;

fn display_help() {
    println!(
        "Usage: yes [STRING]...
Repeatedly output a line with all specified STRING(s), or 'y'.

    -h / --help        display this help and exit
    -v / --version     output version information and exit
    "
    )
}

fn display_version() {
    println!("yes (GNEW coreutils) 0.1")
}

fn display_unknown_flag(s: &str) {
    println!("unrecognized option '{}'", s)
}

fn main() -> ExitCode {
    let mut message: Vec<String> = vec![];

    for arg in env::args().skip(1) {
        if arg.starts_with('-') {
            return match arg.as_str() {
                "-h" | "--help" => {
                    display_help();
                    ExitCode::SUCCESS
                }
                "-v" | "--version" => {
                    display_version();
                    ExitCode::SUCCESS
                }
                s => {
                    display_unknown_flag(s);
                    ExitCode::FAILURE
                }
            };
        }

        message.push(arg.clone());
    }

    let string: String = if !message.is_empty() {
        message.join(" ")
    } else {
        "y".into()
    };

    loop {
        println!("{}", string);
    }
}
