from selenium.webdriver.common.by import By

class Locators():
    # login
    signInTxt = "at_sign_in"
    email = "businessEmail"
    password = "password"
    login = "at_login"
    logout = "userProfileBtn"

    # dashboard
    dashboard = "at_RecentReports"

    in_the_news = "in_the_news"
    all_news_txt = "at_all_news_txt"
    inputCategory_filter = "inputCategory"
    news_by_year = "inputTags"
    news_filter_submit = "news_filter_submit"

    # research library
    sideMenu_researchLib = "at_Research_Library"
    reports = "at_reports"
    search_filter = "at_search_key"
    category_filter = "inputCategory"
    type_filter = "report_type"
    year_filter = "inputYear"
    submit_btn = "at_submit_btn"

    # my ngage
    sideMenu_myNgage = "at_My_Ngage"
    myNgageTxt = "at_myNgage"
    first_report = "/html/body/main/div/div/div/div/div/div[2]/div[1]/div[1]/h4/a"
    at_ViewFullReport = "at_ViewFullReport"

    # report details
    Subscription_Info = "Subscription_Info"

    # order history
    sideMenu_orderHistory = "Orders"
    orderHistoryTxt = "at_orderHistory"

    # Report Downloads
    SideMenu_ReportDownloads = "at_ReportDownloads"
    ReportDownloadsTxt = "at_ReportDownloadsTxt"
    search_rep_downloads = "u_search_key"
    submit_search = "submit-search"

    # wishlist 
    sideMenu_Wish_List = "at_Wish_List"
    wishlistTxt = "at_WishList"

    # my-custom-ngage
    SideMenu_my_custom_ngage = "at_my-custom-ngage"
    myCustomNgageTxt = "at_myCustomNgage"
    MyRequests = "MyRequests"
    myRequestsTxt = "at_myRequests"
    RequestCustomization = "RequestCustomization"
    report_Name = "txtName"
    category = "category"
    description = "txtAbout"
    request_customization_message = "request_customization_message"

    # user guide
    SideMenu_user_Guide = "at_user_Guide"
    userGuideTxt = "at_userGuide"
    userGuideView = "userGuideView"

    # My_Sectors 
    SideMenu_My_Sectors = "at_My_Sectors"
    SubscriptionsTxt = "at_Subscriptions"
    sub_tag = '//*[@id="collapse1"]/div/div[2]/div[1]/div/div/p'
    successmsg = "successmsg"
    errormsg = "errormsg"

    # Dashboard
    SideMenu_Dashboard = "at_Dashboard"

    # profile
    SideMenu_profile = "view_profile"
    profleTxt = "at_profle"
    edit_profile = "edit_profile"
    fullName = "fullName"
    country_id = "country_id"
    txtPhone = "txtPhone"
    txtCompany = "txtCompany"
    txtDesignation = "txtDesignation"
    txtAddress = "txtAddress"
    Save_changes = "Save_changes"
    submit_message = "submit_message"
    changePasswordModal = "at_change_pwd"
    currentPassword = "currentPassword"
    newPassword = "newPassword"
    confirm_password = "confirm_password"
    change_password_btn = "change_password_btn"
    change_password_message = "change_password_message"
    Close_pwd_modal = "Close_pwd_modal"

    # users
    usersTxt = "at_users"
    SideMenu_Users = "Users_List"
    users_search = "at_users_search"
    stats = '/html/body/main/div/div/div/div/div/div[1]/table/tbody/tr[1]/td[7]/a'
    statsTxt = "at_stats"
    users_search_submit = "at_users_search_submit"
    add_org_user = "add_org_user"
    user_full_name = "full_name"
    user_phone_no = "phone_no"
    user_businessEmail = "businessEmail"
    user_job_title = "job_title"
    user_country_id = "country_id"
    user_address = "address"
    user_password = "password"
    user_member_type = "member_type"
    at_save_user = "at_save_user"
    save_user_message ="save_user_message"
    edit_org_user = "/html/body/main/div/div/div/div/div/div[1]/table/tbody/tr[1]/td[8]/a"
    at_edit_user = "at_edit_user"