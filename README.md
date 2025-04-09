# 🔒 Blockchain-Secured ARP

A secure and resilient implementation of the Address Resolution Protocol (ARP) using a private blockchain with Proof of Authority (PoA) consensus to protect local networks against ARP spoofing and Man-in-the-Middle (MITM) attacks.

---

## 📘 Project Summary

This project aims to enhance ARP security by introducing a **blockchain-based verification mechanism** for MAC-IP bindings. Instead of relying on unsecured ARP broadcasts, devices register and validate their MAC-IP associations through digitally signed blockchain transactions. Validators (trusted routers/switches) maintain consensus and approve new bindings in a decentralized yet controlled environment.

---

## 🧱 Key Features

- ✅ **Tamper-proof ARP records** stored on a local blockchain
- 🔑 **Asymmetric encryption** and digital signatures for device authentication
- ⚖️ **Proof of Authority (PoA)** consensus mechanism using VyOS routers as validators
- 🧪 **Simulated WiFi LAN** with Kali and Ubuntu VMs in GNS3
- 🧰 Blockchain backend with **Ganache** and **Node.js** for rapid prototyping

---

## 🧪 Simulation Environment (GNS3)

The project is first prototyped in a **simulated WiFi LAN** using [GNS3](https://www.gns3.com/) on a [Proxmox Hypervisor](https://www.proxmox.com/en/). The simulation includes:

- **VyOS Universal Router** – acts as both DHCP server and blockchain validator
- **Ubuntu VM** – a trusted network client
- **Kali VM** – for simulating spoofing and MITM attacks
- **Ganache** – local blockchain backend
- **Virtual Switch** – connects clients and router in the LAN
- **Cloud Node** – bridges GNS3 network to host WiFi adapter (for internet)

  ---

## 🙋‍♂️ Maintainers
Tanmay Shingavi – [LinkedIn](https://www.linkedin.com/in/tanmay-shingavi/) | [GitHub](https://github.com/decodingafterlife)

