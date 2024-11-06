// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SingleAccountBank {
    address public owner;
    uint public balance;

    constructor() {
        owner = msg.sender;
    }

    function deposit(uint amount) public payable {
        require(msg.sender == owner, "Only the owner can deposit");
        require(amount > 0, "Deposit must be greater than zero");
        balance += amount;
    }

    function withdraw(uint amount) public {
        require(msg.sender == owner, "Only the owner can withdraw");
        require(balance >= amount, "Insufficient balance");
        balance -= amount;
        payable(owner).transfer(amount);
    }

    function checkBalance() public view returns (uint) {
        require(msg.sender == owner, "Only the owner can check balance");
        return balance;
    }
}
