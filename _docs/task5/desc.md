# Task 5: Test Your Dash Application

## What you'll learn
Why good testing is important to avoid unintended consequences when making changes to a codebase

## What you'll do
Create a test suite to verify your Dash app is working as expected

---

## Here is the background information on your task
Testing is the practice of programmatically ensuring the thing you built behaves as expected. Let’s consider a theoretical situation you could find yourself in someday. Consider a potential future where you work on a massive codebase, something with hundreds of thousands of lines of code — countless interconnected components all communicating with each other, passing data back and forth at high speeds in incomprehensible patterns. 

The system is a decade old, and the engineers who originally designed and built it have moved on to other things. Despite having worked on the system for months, its sheer scale has prevented you from completely understanding how every part of the system works. Now suppose you are asked to make a change to the system — modify some esoteric class deep within the bowels of the thing. How would you know your change hasn’t broken some heavily patched component with an obscure relationship to the class you modified? The answer is good testing.

Any production-grade codebase will have an equally robust test suite associated with it. For every granular piece of behaviour in the system, there will be a corresponding collection of tests which ensure it behaves as expected. These tests can be run nigh-instantaneously, and if any slice of code does something unexpected, it will register as a failed test (if properly written). When modifying code, you can run the test suite to ensure you haven’t broken anything. 

It’s one of the many boons of good testing, more of which are described in the linked resources. In this task, your job is to draft a test suite to ensure the visualiser works as expected. These tests may seem trivial, but they are illustrative of an imperative coding practice. Poorly tested production code inevitably leads to sleepless nights for all involved.

---

## Here is your task
1. Your task is to create a test suite to verify your Dash app is working as expected. Using the standard Dash testing framework (documentation linked in the resources below) write three tests which ensure the following:
    - The header is present.
    - The visualisation is present.
    - The region picker is present.
2. Execute your test suite using Pytest and ensure each test passes.
3. Commit and push your changes, then submit a link to your repo below.
