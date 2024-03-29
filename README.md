### Top 
<h1 style="text-align: center;"><strong>Inspa</strong></h1>
<h2 style="text-align: center;"><strong>Welcome to the README PAGE of the Inspa webpage</strong></h2>

### Link to the app:  

<a href="https://inspasite.herokuapp.com">https://inspasite.herokuapp.com</a>

### Link to the GitHub page with Pyramid Game:  

<a href="https://github.com/gretazas/inspa">https://github.com/gretazas/inspa</a>

<p align="center">
<img style="border-radius:50%" width="250" height="250" src="../inspa/static/images/agile/circle.jpg" alt="Green inspirational circle"/>
</p>

# Acknowledgements


# **[Agile thinking](/agile.md)**

# Content

* [Built to inspire](#built-to-inspire)
* [User experience](#user-experience)
* [Buildpacks Used](#buildpacks-used)
* [Frameworks, Libraries & Programs I Used:](#frameworks-libraries-and-programs-i-used)
    * [Random](#random)
    * [Django](#django)
* [Proved by](#proved-by)
* [Features](#features)
* [Future features](#future-features)
* [Deployment](#deployment)
    * [How To Fork A Repository](#how-to-fork-a-repository)
    * [How To Clone A Repository](#how-to-clone-a-repository)
    * [How To Make A Local Clone](#how-to-make-a-local-clone)
* [Testing](#testing)
    *[Unitest](#unitest)
* [Code](#code)
* [Issues and bugs](#issues-and-bugs)
* [Focus group](#focus-group)
* [Contact](#contact)

# Built to inspire

Inspa circle is meant to inspire for greater things in life. To spin great ideas. To help people with anxiety, weightloss, earning extra money, become more healthy. Sometimes we discover things by accident, it would be great if we instatnly could share them with the world Inspa is a platform for sharing and discussing posts related to health, wealth, exercise, and mindfulness. The platform allows users to create and view posts, comment on them, and like them. 

# Getting Started as a user

To get started with Inspa, best way is  to create an account. Once you've created an account, you can start creating posts. To create a post, simply click on the "Add Post" button and enter your post details. To create a comment, simply click on the "Comment" button and in post_detail page you can read all particular post comments, see counts o likes and add your own comment. You would recieve in your random post of the day in your landing page inspa circle. Sure if you dont want to register you account with website, you are still very welcome to give us feedback, read all the posts and visit useful links provided. 

# User stories

- As a site user I can log in so that I can post, comment, and delete messages/ get Inspa of the day.
- As a site user I can register so that I can log in.
- As a site user I can enjoy the view so that I would get inspired by excellent UI and UX.
- As a site member I can post so that can share wisdom and inspiration.
- As a site member I can comment on the posts so that could communicate.
- As a site user I can read posts so that could get ideas and inspiration.
- As a site member I can receive Inspa so that I would get inspiration and wisdom.
- As a site user I can give feedback.
- As a site user I can see inspirational people's names and their descriptions so that I learn about Inspa people.
- As a site user I can view info so that I can contact the company.
- As a site user I can use links so that I can get Inspired by famous speeches.
- As a site user I can view info about youth club members so that I could learn about the team members.
- As a site user I can view posts so that I can benefit from tips.


# Buildpacks Used

- heroku/python

# Frameworks, Libraries and Programs I Used

- Bootstrap
- Django with:
    - gunicorn
    - psycopg2
    - postgresql
    - allAuth
    - Crispy Forms

# Proved By

- <a href="http://pep8online.com/" target="_blank">PEP8: </a> no errors found

<p align="right">(<a href="#top">Back to top</a>)</p>

# Features

- Create and view posts on health, wealth, exercise, and mindfulness
- Comment on posts to start a discussion
- Like posts to show your support
- The Inspa circle with random post o the day.
- Home Page Design
- Website Footer for information
- About Page
- Page with team members
- Internal Web Pages
- Backend Admin
- Logo

# Future features

* In the future I would like to add story: As a site user I can view locations on the map so that I can visit centers.
* To make carousel of Inspa people pictures using JavaScript.

<p align="right">(<a href="#top">Back to top</a>)</p>

# Deployment

This project was deployed using a personal Heroku account.

Steps for deployment:
- Fork or clone this repository
- Create a new Heroku app
- Set the buildpacks to Python and NodeJS in the order
- Link the Heroku app to the repository
- Click on **Deploy**


[How to Fork a Repository:](https://support.atlassian.com/bitbucket-cloud/docs/fork-a-repository/)
1. Login or Sign Up to [GitHub](https://github.com/).
2. On GitHub, go to [https://github.com/gretazas/pyramid](https://github.com/gretazas/pyramid)
3. In the top right corner, click "Fork".

[How to Clone a Repository:](https://support.atlassian.com/bitbucket-cloud/docs/clone-a-repository/)
1. Login in to [GitHub](https://github.com/).
2. Fork the repository [https://github.com/gretazas/pyramid](https://github.com/gretazas/pyramid) using the steps above in [How To Fork a Repository](#how-to-fork-a-repository)
3. Above the file list, click "Code".
4. Choose if you want to close using HTTPS, SSH or GitHub CLI, then click the copy button to the right.
5. Open Git Bash.
6. Change the directory to where you want your clone to go.
7. Type git clone and then paste the URL you copied in step 4.
8. Press Enter to create your clone.

How to make a Local Clone:
1. Login in to [GitHub](https://github.com/)
2. Under the repository name, above the list of files, click "Code".
3. Here you can either Clone or Download the repository.
4. You should close the repository using HTTPS, clicking on the icon to copy the link.
5. Open Git Bash.
6. Change the current working directory to the new location, where you want the cloned directory to be.
7. Type git clone and then paste the URL you copied in step 4.
8. Press Enter and your local clone will be created.

The site was deployed to Github pages using the following steps:
* In the Github repository, navigate to the settings tab.
* Scroll down and select Pages from the left side navigation menu to open Github pages.
* In the Source section, click on the dropdown menu and select the Master branch.
* Once the Master branch is selected the page will refresh to display a message stating "Your site is published at 

<p align="right">(<a href="#top">Back to top</a>)</p>

# Testing

## css validator

<p align="center">
<img width="450" height="350" src="../inspa/static/images/agile/cssvalidatos.jpg" alt="cssvalidator"/>
</p>
<p>
    <a href="https://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>

## html validator

- It shown id="author" dublicated ID, but find in files showns only one, seen in pic provided.<br>
- Same with closing `</p>`, `</a>` tags, looked through all tags with find in files, for few times, not found. Also made suse the wasn\`t like `<a` or `<p` before `</a> ` or `</p>` alo made sure, that it doent contain not allowed tags inside those error marked tags. Eventually `</a>` tag error disapeared, havnt change any tags. <br>
<img width="450" height="350" src="../inspa/static/images/agile/Screenshot(495).png " alt="htmlvalidator"/><br>
<img width="450" height="350" src="../inspa/static/images/agile/Screenshot(496).png " alt="htmlvalidator"/><br>

## lighthouse

<img width="480" height="350" src="../inspa/static/images/agile/Screenshot(499).png " alt="lighthouse"/><br>
<img width="480" height="350" src="../inspa/static/images/agile/Screenshot(500).png " alt="lighthouse"/><br>
<img width="480" height="350" src="../inspa/static/images/agile/Screenshot(501).png " alt="lighthouse"/><br>

## Am I responsive

Issues trying to get responsive design pictures:

<img width="480" height="350" src="../inspa/static/images/agile/Screenshot(502).png " alt="responsive"/><br>
<img width="480" height="350" src="../inspa/static/images/agile/Screenshot(503).png " alt="responsive"/><br>

## Manual testing

- Responsive design, using iphone8 mobile:
    - Go through the pages using navigation bar, writing down issues found
    - Making sure the circle is resizing while going to smaller screen sizes.
- I have manually tested this project by doing the following:
- Passed the code through a PEP8 linter and confirmed there are no problems.
- Given invalid inputs: strings when numbers are expected. Feedback email must be correct form. registration form must be correct. To post a post must fill all required form inputs. for comment email must be legit.
- Press buttons, make usre they work. Submit feedback form, post, comment, add cmment in post detail page, login, register, logput. Browse throug nav, footer, sign out page links.
- Add post as a member, and try to add post as a user(get message:  must be logged in to proceed), same with comment button in posts page.

# Code

Inspiration for the project came from my daughter. She has anxiety. Hope website would be helpful to many people.

**[Code explained in detail](./functions.md)**

* All code was written by myself and was learned from [www.codeinstitute.net](https://www.codeinstitute.net).

# Issues and bugs

* I came back to my project after good while after I`ve started it and had to reinstal all instalations and set Herolu dynos and postgres, caused alot of issues.
* Using feed back in index.html used to get  errorMethod Not Allowed (GET): /feedback/, but no error in the form. Fixed with feedback_form.instance.email = request.user.email.
* Couldnt hide email field for authenticated users in feedback form. Tired to add self.fields['email'].widget = forms.HiddenInput() in def __init__(self, *args, **kwargs) function.
<br>

<p align="right">(<a href="#top">Back to top</a>)</p>

# Focus Group

* I'd like to thank the following people for the help they gave me with this project:
  - My daughter Madelyne for helping me with README.md page <br>
  - John, Alex, and Gemma from Code Institute Tutor Assistance.<br>
  - Help from Code Institute Slack app: 
        DaveHarricks_ci, Sean YOUng_aluminati, Ian Meigh_5p,
        Eventyret_mentor, DaveHorocks_5p, Manni_alumnus

  <img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" width="90">
  
 
# Contact 

![](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white) https://github.com/gretazas<br>
Greta Baliunaite: [ https://www.facebook.com/greta.baliunaite]( https://www.facebook.com/greta.baliunaite)

<br>
<br>

![Safe](https://img.shields.io/badge/Stay-Safe-red?logo=data:image/svg%2bxml;base64,PHN2ZyBpZD0iTGF5ZXJfMSIgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAwIDAgNTEwIDUxMCIgaGVpZ2h0PSI1MTIiIHZpZXdCb3g9IjAgMCA1MTAgNTEwIiB3aWR0aD0iNTEyIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxnPjxnPjxwYXRoIGQ9Im0xNzQuNjEgMzAwYy0yMC41OCAwLTQwLjU2IDYuOTUtNTYuNjkgMTkuNzJsLTExMC4wOSA4NS43OTd2MTA0LjQ4M2g1My41MjlsNzYuNDcxLTY1aDEyNi44MnYtMTQ1eiIgZmlsbD0iI2ZmZGRjZSIvPjwvZz48cGF0aCBkPSJtNTAyLjE3IDI4NC43MmMwIDguOTUtMy42IDE3Ljg5LTEwLjc4IDI0LjQ2bC0xNDguNTYgMTM1LjgyaC03OC4xOHYtODVoNjguMThsMTE0LjM0LTEwMC4yMWMxMi44Mi0xMS4yMyAzMi4wNi0xMC45MiA0NC41LjczIDcgNi41NSAxMC41IDE1LjM4IDEwLjUgMjQuMnoiIGZpbGw9IiNmZmNjYmQiLz48cGF0aCBkPSJtMzMyLjgzIDM0OS42M3YxMC4zN2gtNjguMTh2LTYwaDE4LjU1YzI3LjQxIDAgNDkuNjMgMjIuMjIgNDkuNjMgNDkuNjN6IiBmaWxsPSIjZmZjY2JkIi8+PHBhdGggZD0ibTM5OS44IDc3LjN2OC4wMWMwIDIwLjY1LTguMDQgNDAuMDctMjIuNjQgNTQuNjdsLTExMi41MSAxMTIuNTF2LTIyNi42NmwzLjE4LTMuMTljMTQuNi0xNC42IDM0LjAyLTIyLjY0IDU0LjY3LTIyLjY0IDQyLjYyIDAgNzcuMyAzNC42OCA3Ny4zIDc3LjN6IiBmaWxsPSIjZDAwMDUwIi8+PHBhdGggZD0ibTI2NC42NSAyNS44M3YyMjYuNjZsLTExMi41MS0xMTIuNTFjLTE0LjYtMTQuNi0yMi42NC0zNC4wMi0yMi42NC01NC42N3YtOC4wMWMwLTQyLjYyIDM0LjY4LTc3LjMgNzcuMy03Ny4zIDIwLjY1IDAgNDAuMDYgOC4wNCA1NC42NiAyMi42NHoiIGZpbGw9IiNmZjRhNGEiLz48cGF0aCBkPSJtMjEyLjgzIDM2MC4xMnYzMGg1MS44MnYtMzB6IiBmaWxsPSIjZmZjY2JkIi8+PHBhdGggZD0ibTI2NC42NSAzNjAuMTJ2MzBoMzYuMTRsMzIuMDQtMzB6IiBmaWxsPSIjZmZiZGE5Ii8+PC9nPjwvc3ZnPg==)

<p align="right">(<a href="#top">Back to top</a>)</p>
