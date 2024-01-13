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
                clear()
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
            "username":username,
            "password":password
        }
    def loginfail(self):
        print("login failed")
    def loginsucc(self):
        print("login_succ")



class dashboard_view:
    def select_post_delete(self):
        selected_post = input('SELECT_POST_TO_DELETE: ')
        return selected_post
    def del_post_list(self,postnum,content):
        print(f'POST #{postnum}')
        print(f'CONTENT: {content}')
        print()
    def update_post(self,postnum,content):
        print(f'POST #{postnum}')
        print(f'CONTENT: {content}')
        print()
    def update_select_post(self):
        select_post_update = input('SELECT POST TO EDIT: ')
        return int(select_post_update) -1
    def content_edit(self):
        update_content = input('UPDATED_CONTENT: ')
        return update_content

    def update_delete_succ(self,messege):
        input(messege)
    def update_delete_fail(self,messege):
        input(messege)
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
            for cindex in range(len(comments)):
                if comments[cindex]["post_index"] == pindex:
                    print("  COMMENT:")
                    comment_author_index = comments[cindex]['author_id']
                    comment_author_name = user[comment_author_index]["username"]
                    comment = comments[cindex]['comment']
                    print(f'    Author: {comment_author_name}')
                    print(f'        {comment}')
                else:
                    pass
            print()
        print('TYPE -e- FOR EXIT')
        post_select = input("SELECT POST TO COMMENT: ")
        return (post_select)

    def select_dashboard_option(self):
        print('''
        TYPE -l- TO LOGOUT
        Select Dashboard Option
1). VIEW_POST_AND_COMMENT   2). CREATE_POST    3). UPDATE_POST   4). DELETE_POST ''')
        option = input("Option: ")
        return (option)
    
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
        clear()
        post_selection = self.view.view_posts(
            self.model["Posts"].get_posts(),
            self.model["comment"].get_all_comments(),
            self.model["users"].read_user()
        )
        if post_selection.lower() == 'e':
            self.start_dashboard()
        clear()
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
                    self.view.update_delete_fail('YOU ARE NOT THE AUTHOR ON SELECTED COMMENT')
                    self.friends_post()
                    comments.clear()
                else:
                    comment_update = input('UPDATED_COMMENT: ')
                    selected_comment_update = comments[select_comment -1]
                    main_comment_model_index = selected_comment_update['comment_index']
                    self.model['comment'].get_all_comments()[main_comment_model_index]['comment'] = comment_update
                    self.view.update_delete_succ('COMMENT UPDATED')
                    self.friends_post()
                    comments.clear()
            elif comment_option == 3:
                select_delete_comment = input('SELECT COMMENT: ')
                if self.current_user_index != comments[int(select_delete_comment)-1]['author_id']:
                    self.view.update_delete_fail('YOU ARE NOT THE AUTHOR ON SELECTED COMMENT')
                    self.friends_post()
                else:
                    delcom_comment_selected = comments[int(select_delete_comment)-1]
                    main_comment_model_index_to_del = delcom_comment_selected['comment_index']
                    self.model['comment'].get_all_comments().pop(main_comment_model_index_to_del)
                    self.friends_post()
                
                

        except NameError:
            pass

    def create_comment(self,current_user,post_index,comment):
        self.model['comment'].create_comment(current_user,post_index,comment)

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
        clear()
        self.view.print_current_user(
            self.model["users"].read_user()[self.current_user_index]["username"]
            )
        option = self.view.select_dashboard_option()
        if str(option.lower()) == 'l':
            clear()
            return
        elif int(option) == 2:
            self.create_post()
        
        elif int(option) == 3:
            U_post = []
            
            post_model = self.model['Posts'].get_posts()
            for pindex in range(len(post_model)):
                if post_model[pindex]['author_id'] == self.current_user_index:
                    post_model[pindex]['post_model_index'] = pindex
                    U_post.append(post_model[pindex])
                    post_num = pindex +1
                    content = post_model[pindex]['post']
                    self.view.update_post(post_num,content)
                        
                else:
                    pass
            if U_post == []:
                input('No Post Created')
                self.start_dashboard()
            else:
                selected_post = self.view.update_select_post()
                updated_content = self.view.content_edit()
                post_model_index = U_post[selected_post]['post_model_index']
                self.model['Posts'].get_posts()[post_model_index]['post'] = updated_content
                self.start_dashboard()
        #update post
        elif int(option) == 4:
            D_post = []
            for i in range(len(self.model['Posts'].get_posts())):
                if self.model['Posts'].get_posts()[i]['author_id'] == self.current_user_index:
                    self.model['Posts'].get_posts()[i]['post_model_index'] = i
                    D_post.append(self.model['Posts'].get_posts()[i])
                    post_num_del = i +1
                    content_del = self.model['Posts'].get_posts()[i]['post']
                    self.view.del_post_list(post_num_del,content_del)
            if D_post == []:
                input('NO POST CREATED')
                self.start_dashboard()
            else:
                try:
                    selected_post_del = self.view.select_post_delete()
                    self.model['Posts'].get_posts().pop(D_post[int(selected_post_del) -1]['post_model_index'])
                    print('POST DELETED')
                    self.start_dashboard()
                except:
                    print('INVALID INPUT')
                    self.start_dashboard()

        #delete post

        elif int(option) == 1:# for view posts
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
        try:
            option = Auth_controller.sel_option()
            if option >= 3:
                input('INVALID INPUT PRESS ENTER TO CONTINUE')
            elif option == 1:
                current_user_index = Auth_controller.login()
                if current_user_index is not None:
                    AuthLoop = False
                    Dashboard_controller = dashboard_controller(
                        view=Dashboard_view,
                        model=Dashboard_models,
                        current_user_Index=current_user_index,
                    )
                    Dashboard_controller.start_dashboard()
                    AuthLoop = True
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
        except:
            input('INVALID INPUT PRESS ENTER TO CONTINUE')
            clear()

        


