import os

clear = lambda: os.system('cls')

class datauser:
    def __init__(self):
        self.users = [
            {
                "username":"felbert",
                "password":"felbert14",
            },
            {
                "username":"Melbert",
                "password":"Melbert14"
            },
            {
                "username":"Jelbert",
                "password":"Jelbert14"
            },
            {
                "username":"Pelbert",
                "password":"Pelbert14"
            },
            {
                "username":"Telbert",
                "password":"Telbert14"
            }
        ]
    def authentication(self,username,password):
        for i,user in enumerate(self.users):
            if username == user["username"] and password == user["password"]:
                return i
            else:
                if i == len(self.users)-1:
                    return None
    def create_user(self,username,password):
        self.users.append(
            {
                "username":username,
                "password":password
            }
        )
    def read_user(self):
       return self.users



class userpost(datauser):
    def __init__(self):
        super().__init__()
        self.posts = [
            {
                "author_id":0,
                "post":"hello_earth"
            },
            {
                "author_id":1,
                "post":"Hello_Universe"
            }
        ]
    def create_user_post(self,post,user_index):
        self.posts.append(
            {
                "author_id":user_index,
                "post":post
            }
        )
    def delete_post(self,post_index):
        self.posts.pop(post_index)
    def update_post(self,post_index,updated_post):
        self.posts[post_index]["post"] = updated_post
    def get_posts(self):
        return self.posts
    def getallusers(self):
        return super().read_user()
    
class comment(userpost):
    def __init__(self):
        super().__init__()
        self.comments = [
            {
                "author_id":0,
                "post_index":3,
                "comment":"here's the comment :)"
            },
            {
                "author_id":2,
                "post_index":0,
                "comment":"hello buddy:)"
            },
            {
                "author_id":0,
                "post_index":1,
                "comment":"hello :)"
            },
            {
                "author_id":0,
                "post_index":1,
                "comment":"hfsdf :)"
            }
            
        ]
    def get_all_comments(self):
        return self.comments
    
    def create_comment(self,user_index,post_index,comment):
        self.comments.append(
            {
                "author_id":user_index,
                "post_index":post_index,
                "comment":comment
            }
        )
    def delete_comment(self,comment_index):
        self.comments.pop(comment_index)

    def update_comment(self,comment_index,comment_update):
        self.comments[comment_index] = comment_update

#c  
    
class auth_controller:

    def __init__(self,view,model):
        self.view = view
        self.model = model

    def register(self):
        rg = self.view.register()
        username = rg["username"]
        password = rg["password"]
        confirm_password = rg["confirm_password"]
        
        if password == confirm_password:
            self.model.create_user(username, confirm_password)
            self.view.register_confirm_pass_success()
            return True
        else:
            register_option = self.view.register_confirm_pass_fail()
            if register_option != "":
                return False
            else:
                return True


    def login(self):
        lg=self.view.login()
        username=lg["username"]
        password=lg["password"]
        verify = self.model.authentication(username,password)
        if verify != None:
            self.view.loginsucc()
            return int(verify)
        else:
            self.view.loginfail()
            return verify

    def sel_option(self):
        option = self.view.auth_sel_options()
        if option == 1:
            return 1
        if option == 2:
            return 2
        else:
            return None


#v
class auth_view:

    def auth_sel_options(self):
        print("""
        S E L E C T    O P T I O N S
    
    1) Login        2)Register
        """)

        option = input("Option: ")
        option = int(option)
        return option
    
    def register(self):
        print("""
        R E G I S T E R
              """)
        username = input("Username: ")
        password = input("password: ")
        confirm_password = input("Confirm_Password: ")
        return {
            "username":username,
            "password":password,
            "confirm_password":confirm_password
        }
    
    def register_confirm_pass_fail(self):
        print("password and confirm password is not the same")
        reg_option = input("Press Enter to continue or input 0 to exit: ")
        return reg_option
    def register_confirm_pass_success(self):
        print("Register Successful")

############################################

    def login(self):
        username = input("Username: ")
        password = input("Password: ")
        return {
            "username":'felbert',
            "password":'felbert14'
        }
    def loginfail(self):
        print("login failed")
    def loginsucc(self):
        print("login_succ")



class dashboard_view:
    
    def comment_update(self):
        pass
    def print_selected_post(self,author,content,comments,user):
        print(f'AUTHOR: {author}')
        print(f'CONTENT: {content}')
        for ci in range(len(comments)):
            print(f'COMMENT NO.{ci +1}')
            comment_author_index = comments[ci]['author_id']
            comment_author_username = user[comment_author_index]['username']
            comment = comments[ci]['comment']
            print(f' AUTHOR: {comment_author_username}')
            print(f' {comment}')

        
    def comment_option(self):
        print('1). CREATE COMMENT  2). UPDATE  3). DELETE')
        option = input('OPTION: ')
        return option

    def print_current_user(self,current_username):
        print(f'''CurrentUser: {current_username}

''')
    def comment_decision_error(self):
        print()
    def view_post_selection(self,comment_sel_index,post,comment):
        print(post[int(comment_sel_index)]["post"])
        for c in range(len(comment)):
            if comment[c]["post_index"] == int(comment_sel_index):
                print()
                print(f'comment #{c}')
                print(f'  author: {comment[c]["author"]}')
                print(f'    comment: {comment[c]["comment"]}')
                print("-")
        print("0.) Exit    1.) edit_post   2.) delete_post")
        comment_des = input('select comment option: ')
        return comment_des

        

    def view_posts(self,posts,comments,user):
        print('''      𝑷 𝑶 𝑺 𝑻 𝑺  ''')
        print()
        for pindex in range(len(posts)):
            print(f'POST# {pindex +1}')
            Author = user[posts[pindex]["author_id"]]["username"]
            content = posts[pindex]["post"]
            print(f'Author: {Author}')
            print(f'Content: {content}')
            print(' Comments:')
            for cindex in range(len(comments)):
                if comments[cindex]["post_index"] == pindex:
                    comment_author_index = comments[cindex]['author_id']
                    comment_author_name = user[comment_author_index]["username"]
                    comment = comments[cindex]['comment']
                    print(f'Author: {comment_author_name}')
                    print(f' {comment}')
                else:
                    pass
            print()
        post_select = input("SELECT POST TO COMMENT: ")
        return (post_select)

    def select_dashboard_option(self):
        print('''
        Select Dashboard Option
1). CREATE POST        2). VIEW POST AND COMMENT''')
        option = input("Option: ")
        
        return int(option)
    
    def create_post(self):
        print("0). Cancel")
        content = input("Content: ")
        return content
    def create_post_option(self):
        print("Content uploaded")
    
    def content_empty(self):
        input("content is empty! press Enter to Continue")





class dashboard_controller:
    def __init__(self,view,model,current_user_Index):
        self.model = model
        self.view = view
        self.current_user_index = current_user_Index

    def friends_post(self):
        self.view.print_current_user(
        self.model["users"].read_user()[self.current_user_index]["username"]
        )
        post_selection = self.view.view_posts(
            self.model["Posts"].get_posts(),
            self.model["comment"].get_all_comments(),
            self.model["users"].read_user()
        )
        try:
            post_index = self.model['Posts'].get_posts()[int(post_selection) -1]
            author_index = post_index['author_id']
            author = self.model['users'].read_user()[author_index]['username']
            post_content = post_index["post"]
            comment_model = self.model['comment'].get_all_comments()
            user_model = self.model['users'].read_user()
            comments = []

            for cindex in range(len(comment_model)):
                if comment_model[cindex]['post_index'] == int(post_selection) -1:
                    comment_add = comment_model[cindex]
                    comment_add['comment_index'] = cindex
                    comments.append(comment_add)
                else:
                    pass

            
            self.view.print_selected_post(author,post_content,comments,user_model)
            comment_option = self.view.comment_option()
            comment_option = int(comment_option)
            if comment_option == 1:
                comment_input = input('COMMENT: ')
                self.create_comment(current_user=self.current_user_index,post_index=int(post_selection)-1,comment=comment_input)
                self.friends_post()
            elif comment_option == 2:
                select_comment = input('SELECT COMMENT NO:')
                select_comment = int(select_comment)
                if self.current_user_index != comments[select_comment -1]['author_id']:
                    print('YOU ARE NOT THE AUTHOR IN THIS COMMENT')
                else:
                    pass
                self.update_comment()
            elif comment_option == 3:
                self.delete_comment()

        except:
            input('INVALID INPUT: PRESS ENTER TO CONTINUE')
            self.friends_post()

    def create_comment(self,current_user,post_index,comment):
        self.model['comment'].create_comment(current_user,post_index,comment)
    def update_comment(self,current_user,updated_comment,comment_index):
        pass
    def delete_comment(self,current_user,comment_index):
        pass


        

    def create_post(self):
        postloop = True
        while postloop:
            content = self.view.create_post()
            if content == "0":
                self.start_dashboard()
                postloop = False
            elif content == "":
                self.view.content_empty()
                postloop = True
            elif content != "":
                self.model["Posts"].create_user_post(content,self.current_user_index)
                postloop = False
                self.start_dashboard()

    def start_dashboard(self):
        self.view.print_current_user(
            self.model["users"].read_user()[self.current_user_index]["username"]
            )
        option = self.view.select_dashboard_option()
        if option == 1:
            self.create_post()
            
        elif option == 2:# for view posts
            self.friends_post()
            

        

if __name__ == "__main__":

    userdata = datauser()
    comment_data = comment()
    posts_data = userpost()

    Auth_view = auth_view()
    Auth_controller = auth_controller(view=Auth_view, model=userdata)
    
    Dashboard_view = dashboard_view()
    Dashboard_models = {
        "users": userdata,
        "comment": comment_data,
        "Posts": posts_data
    }
    
    AuthLoop = True
    while AuthLoop:
        option = Auth_controller.sel_option()
        if option == 1:
            current_user_index = Auth_controller.login()
            if current_user_index is not None:
                AuthLoop = False
                Dashboard_controller = dashboard_controller(
                    view=Dashboard_view,
                    model=Dashboard_models,
                    current_user_Index=current_user_index,
                )
                Dashboard_controller.start_dashboard()
            else:
                AuthLoop = True
                clear()
        elif option == 2:
            Register_Loop = True
            while Register_Loop:
                clear()
                register_successful = Auth_controller.register()
                if register_successful is not True:
                    Register_Loop = True
                    AuthLoop = True
                    clear()
                else:
                    Register_Loop = False
                    AuthLoop = True


