use std::env;
use std::fs::File;
use std::io::{self, Read, BufReader};
use std::net::{TcpListener, TcpStream};
use std::thread;
use std::io::Write;

fn read_file(path: &str) -> String {
    let file = File::open(path);
    if file.is_err() {
        return "ERROR".to_string();
    }
    
    let mut reader = BufReader::new(file.unwrap());
    let mut contents = String::new();
    
    if reader.read_to_string(&mut contents).is_err() {
        return "ERROR".to_string();
    }
    
    contents
}

fn handle_client(mut stream: TcpStream, contents: &str) -> io::Result<()> {
    // Read the request to avoid connection reset issues
    let mut buffer = [0; 512];
    stream.read(&mut buffer)?;

    // Formulate the response with proper HTTP headers
    let response = format!(
        "HTTP/1.1 200 OK\r\nContent-Length: {}\r\nContent-Type: text/plain\r\nConnection: close\r\n\r\n{}",
        contents.len(),
        contents
    );

    stream.write_all(response.as_bytes())?;
    stream.flush()?;
    Ok(())
}

fn content_stream(contents: String) -> io::Result<()> {
    let listener = TcpListener::bind("127.0.0.1:32666")?;
    println!("Server listening on port 32666");

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                let contents = contents.clone();
                thread::spawn(move || {
                    handle_client(stream, &contents).unwrap_or_else(|error| eprintln!("{:?}", error));
                });
            }
            Err(e) => {
                eprintln!("Connection failed: {:?}", e);
            }
        }
    }

    Ok(())
}

fn main() -> io::Result<()> {
    // Get the file path from the command-line arguments or default to "main.z0s"
    let args: Vec<String> = env::args().collect();
    let path = if args.len() > 1 {
        &args[1]
    } else {
        "./main.z0s"
    };

    let contents = read_file(path);
    content_stream(contents)
}
