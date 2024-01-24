# Trying out web servers

# How to set up a domain name
## In our case we'll be using .tech domains as a domain provider
-Step1: Access the link to your Github Student Developer Pack provided to you by your school and register.

- Step2: In the Github Education landing page, access the `Students` drop-down option and select  `Get Your Student Developer Pack`

- Step3: Scroll down and find `.tech Domains`, and click on the link that connects your Github account on .TECH

- Step3: From `get.tech` web page search for any domain name you wish and if it's available click on it and add it to cart. You've successfully purchased a domain name


## Configure Domain
- Step1: Go to the `get.tech` page and select the account option and if you're logged in it will redirect you to your domain managing page

- Step2: Click on `Manage Orders` then `List/Search Orders`

- Step3: click on the Domain Name you chose, scroll down to find the `DNS Management` option then `Manage DNS`

- Step4: Manage the Records as you wish. In my case I Added an `A Record`, added my `server_IP_address` in the `Destination IPv4 Address` input.

- Step5: Gave it a few minutes and accessed my server using the domain name in any browser

## Confirm in Ubuntu terminal
- Run `dig [insert_your_domain_name]`


NB: When your domain name is setup, please verify the Registrar here: `https://whois.whoisxmlapi.com/` and you must see in the JSON response: `"registrarName": "Dotserve Inc"`
