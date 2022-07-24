use clap::Parser;

#[derive(Parser)]
#[clap(name = "yes")]
#[clap(author = "GDWR <gregory.dwr@gmail.com>")]
#[clap(version = "1.0")]
struct Cli {
    /// The string to repeat, defaults to 'y'
    string: Option<String>,
}

fn main() {
    let cli = Cli::parse();
    let value = cli.string.unwrap_or_else(|| String::from("y"));

    loop {
        println!("{}", value);
    }
}
