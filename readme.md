# **z0 script** - *Zota0's* scripting language

## **Why?**

### Just because

## **For what?**

### IDK

## **Installation?**

### You need: 
- Python **3.11** *or higher*,
- **Rust** with **Cargo** *(if not using Windows or want to build from source)*
-  free port **`32666`** (localhost|127.0.0.1) <- or else you need to change files: <br />`src/rust/file_reader.rs` and `src/python/listener.py` .

#### **USING PRE-BUILT EXECUTABLE** *(Only Windows)*

1. Clone repository

2. Go to `scripts/`

3. Reading scripts:
    * If you want to open default file: `main.z0s` then open `file_reader.exe`,

    * If you want to open custom/specific file then open via cmd with `file_reader.exe -- <relative path to file>` <br /> **NOTE:** *You can place `file_reader.exe` anywhere you want, because it doesnt need to be in `scripts/` folder, but code file needs to be in relative path*

4. Run `main.py` from `src/python/` folder

5. Your code is running 😃

---

#### **BUILDING `file_reader` FROM SOURCE** *(needed **Rust** with **Cargo**)*

1. Clone repository

2. Go to `src/rust/`

3. Run `cargo build -r`

4. Open `src/rust/target/release/`

5. Move `file_reader` file to `scripts/` <br /> *(or else you need to place z0 script file in `src/rust/target/release` folder)*

7. Go to `scripts/`

8. Reading scripts:
    * If you want to open default file: `main.z0s` then open `file_reader` file,

    * If you want to open custom/specific file then open via cmd with `./file_reader -- <relative path to file>` <br /><br /> **NOTE:** *You can place `file_reader` anywhere you want, because it doesnt need to be in `scripts/` folder, but code file needs to be in relative path*

9. Run `main.py` from `src/python/` folder

10. Your code is running 😃

---

## Example code

``` z0s
#log("Hello, World!");
```