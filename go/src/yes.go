package main

import (
	"fmt"
	"github.com/alexflint/go-arg"
)

const NAME = "yes"
const VERSION = "1.0"
const AUTHOR = "<GDWR gregory.dwr@gmail.com>"

func main() {
	var args struct {
		Version bool `arg:"-v,--version" help:"display version information and exit"`

		String string `arg:"positional"`
	}
	arg.MustParse(&args)

	if args.Version {
		fmt.Println(NAME, "(GNEW coreutils)", VERSION)
		fmt.Println("Written by", AUTHOR)
		return
	}

	for {
		println(args.String)
	}

}
