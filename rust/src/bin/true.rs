use std::env;
use std::process::ExitCode;

fn display_help() {
    println!(
        "Usage: true 
Exit with a status code indicating success.

    -h / --help        display this help and exit
    -v / --version     output version information and exit
    "
    )
}

fn display_version() {
    println!("true (GNEW coreutils) 0.1")
}

fn display_unknown_flag(s: &str) {
    println!("unrecognized option '{}'", s)
}

fn main() -> ExitCode {
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
                _ => ExitCode::SUCCESS,
            };
        }
    }

    ExitCode::SUCCESS
}
