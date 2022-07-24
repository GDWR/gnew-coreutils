use clap::Parser;

#[derive(Parser)]
#[clap(name = "false")]
#[clap(author = "GDWR <gregory.dwr@gmail.com>")]
#[clap(version = "1.0")]
struct Cli {}

fn main() {
    Cli::parse();
    std::process::exit(1);
}
