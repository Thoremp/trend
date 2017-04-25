# coding=utf-8

import MySQLdb
from DBUtils.PooledDB import PooledDB
pool = PooledDB(MySQLdb, 10, host='120.25.103.83',user='root',passwd='Astarmo826@',db='trend',port=3306,charset='utf8') #5为连接

# 持久化 trend_usa 一条记录
# 入参:result 数组
def saveMessage(result):
    conn = pool.connection()
    cur = conn.cursor()

    sql = '''
        insert into trend_basis_usa(addTime,deleteStatus,recruitUrl,title,companyUrl,companyName,address,releaseDate)
        values(now(), 0, %s,%s,%s,%s,%s,%s)
    '''
    cur.execute(sql, result)

    cur.close()
    conn.commit()
    conn.close()

# 根据 recruitUrl 查询 trend_basis_usa 中的数据(是否存在)
def isHaveRecruitUrl(recruitUrl):
    conn = pool.connection()
    cur = conn.cursor()

    sql = "select * from trend_basis_usa where 1=%s and recruitUrl=%s"
    count = cur.execute(sql, (1,recruitUrl))

    cur.close()
    conn.commit()
    conn.close()
    return count


html = """

<!DOCTYPE html>
<html xmlns="https://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>


    <meta http-equiv="X-UA-Compatible" content="IE=8, IE=9, IE=10" />
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta http-equiv="Expires" content="0" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1" />
<meta charset="utf-8">
<link type="text/css" rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500">


<!--[if IE 8]>
      <link rel="stylesheet" type="text/css" href="https://securemedia.newjobs.com/niche/css/generic-template/style-ie.css" />
<![endif]-->

<!--[if lt IE 9]>
<script src="https://securemedia.newjobs.com/niche/js/html5shim.js"></script>
<script src="/siteassets/scripts/respond.js" type="text/javascript"></script>
<![endif]-->

    <script src="https://oas.monster.com/Scripts/oas_analytics.js" type="text/javascript"></script>


<title>Python Jobs | Monster.com</title>
    <link rel="canonical" href="https://www.monster.com/jobs/q-python-jobs.aspx" />
<link id="favIcon" runat="server" rel="shortcut icon" href="https://securemedia.newjobs.com/favicon.ico" />
<meta name="description" content="Explore more than 1,000 Python jobs in the United-States. Browse by location or industry. Find the right position and build your career." />
<meta name="keywords" content="Python jobs, Python career resources, Python careers, Python job, Python career, Python employment, Python work, Python job opportunities, Python employment opportunities, jobs in Python, careers in Python" />
<meta name="SL.domain" content = "login.monster.com" />
<meta name="SL.channelAlias" content="MONS" />
    <meta content="Python Jobs | Monster.com" property="og:title" />
    <meta content="website" property="og:type" />
    <meta content="https://www.monster.com/jobs/search/?q=Python" property="og:url" />
    <meta content="https://securemedia.newjobs.com/id/lpf20/CORE/icon-50-m.png" property="og:image" />
    <meta content="Monster" property="og:site_name" />
    <meta content="Explore more than 1,000 Python jobs in the United-States. Browse by location or industry. Find the right position and build your career." property="og:description" />
    <meta content="Python Jobs | Monster.com" itemprop="name" />
    <meta content="Explore more than 1,000 Python jobs in the United-States. Browse by location or industry. Find the right position and build your career." itemprop="description" />
    <meta content="https://securemedia.newjobs.com/id/lpf20/CORE/icon-50-m.png"  itemprop="image" />
    <link rel="next" href="https://www.monster.com/jobs/search/?q=Python&amp;page=2" />
    <link href="https://css-seeker.newjobs.com/MONS/v4.1.2.8/lpf30.v2_css.axd?s=1" type="text/css" rel="stylesheet" />
    <script type="text/javascript" src="https://js-seeker.newjobs.com/MONS/v4.1.2.34/lpf30_js.axd?s=1"></script>







<meta content="Monster" name="m_impr.a_affiliate_id" /><meta content="q=Python&amp;brd=1&amp;brd=2&amp;cy=US&amp;pp=25&amp;sort=rv.di.dt&amp;stp=TwoBoxBand" name="m_impr.s_search_query" />
<meta content="Python" name="m_impr.s_q" />
<meta content="1" name="m_impr.j_pg" />











<script type="text/javascript" src="//nexus.ensighten.com/monster/Bootstrap.js"></script>



<meta name="debugInfo" content="
"/>

    <script type="text/javascript">
       var inHeadTS = (new Date()).getTime();
    </script>
        <script type="text/javascript">
        var navResult = {"Result":{"ChannelId":58,"ChannelAlias":"MONS","NavHeader":null,"NavFooter":null},"Status":"Success","ErrorDetails":"Success","ErrorGuid":""};
        if (navResult.Result.NavHeader != null) {
            document.write ("<link rel='stylesheet' type='text/css' href='https://securemedia.newjobs.com/global/css/www/newspaper-nav/newspaper-nav.css' />");
            document.write("<style>.mainbar .matter{margin-top: 0;} .logo-newspaper {background: url('" + navResult.Result.NavHeader.NpLogoImageUrl + "') no-repeat scroll center center / contain} .jobAlertButton {top:112px} @media (max-width: 767px) { .logo-newspaper {height: 50px; margin-left:0;} .navbar.solid-nav .navbar-text.login-btn {margin-top: 8px;} .navbar .navbar-toggle.search-btn-container {margin: 7px 0 0;} body {margin-top: 146px !important;} .jobAlertButton {top: 120px;} }</style>");
        }
    </script>

</head>
<body class="card-view-2">
<script type="text/javascript" language="javascript">var DYNAMIC_S_ACCOUNT='newjobsProdSeekerUS';var DYNAMIC_S_CURRENCYCODE='USD';</script><script type="text/javascript">//<![CDATA[
var amc=amc||{};if(!amc.on){amc.on=amc.call=function(){}};
document.write("<scr"+"ipt type='text/javascript' src='https://securemedia.newjobs.com/js/sc/targetsitecatalystloadtimeLL.js'></sc"+"ript>");
//]]>
_m.ATM.properties={"eVar2":"unrecognized","channel":"58","eVar1":"D=g","prop1":"D=g","eVar4":"0","eVar17":"Unspecified","eVar16":"trovix-cloud-band","eVar23":"1001+","eVar19":"Python","eVar24":"1","eVar18":"Unspecified","events.event1":"jobsearch","eVar20":"Unspecified","list2":"Unspecified","list1":"Unspecified","eVar21":"Unspecified","prop16":"Unspecified","prop17":"Unspecified","prop18":"Unspecified","prop19":"Unspecified","eVar22":"Unspecified","events.event27":"true","eVar69":"NewCardView","list3":"ViewSplit_NewCardView,BAMLiteSplit_Default,TypeaheadElasticSearchSplit_NewElasticSearch","eVar43":"Cloud Search Y"};_m.ATM.pageName='desktop|mons|lpf|jobsearch-trovix-cloud-band';_m.ATM.version=0;_m.ATM.appID='lpf';_m.ATM.channelID=58;_m.ATM.countryID=164;_m.ATM.appConfig={version:'0',appID:'lpf',channelID:'58',countryID:'164'};_m.ATM.runOnLoad=true;
(function () {if (typeof _m.ATM.initFromOnReady === 'function') {_m.ATM.initFromOnReady();} else {setTimeout(function () {if (typeof _m.ATM.initFromOnReady === 'function') {_m.ATM.initFromOnReady();} else {$(document).ready(_m.ATM.initFromOnReady);}}, 200);}})();</script>


<!-- Google Tag Manager -->
<noscript><iframe src="//www.googletagmanager.com/ns.html?id=GTM-NQK2FJ"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-NQK2FJ');</script>
<!-- End Google Tag Manager -->



<div style="display:none;"></div>

    <!-- start of markup for nano ad -->

    <script type="text/javascript" language="JavaScript">
        $(function () {
            _s.lpf.canTrack.trackI();
        });
    </script>

<!-- end of markup for nano ad -->


<a href="#mainContent" class="skip-main">Skip to main content</a>








    <div id="headerWidget">


<input type="hidden" id="AcceptCookies" value="True" />

<input type="hidden" id="lpfDomainPath" value="https://www.monster.com/jobs" />
<input type="hidden" id="servicesDomainPath" value="https://www.monster.com/jobs" />
<input type="hidden" id="inboxLink" value="https://www.monster.com/message/inbox" />
<input type="hidden" id="countryId" value="164" />
<input type="hidden" id="showLocationTypeAheadTrovix" value="True" />
<input type="hidden" id="showLocationTypeAheadLucene" value="False" />
<input type="hidden" id="showKeywordTypeAheadTrovix" value="True" />
<input type="hidden" id="isLoggedIn" value="False" />
<input type="hidden" id="isOnlyRecognized" value="False" />
<input type="hidden" id="successMessage" value="You have no new messages." />
<input type="hidden" id="cookieName" value="hdCookiesIM" />
<input type="hidden" id="cookieValue" value="0" />
<input type="hidden" id="cookieExpirationTime" value="365" />
<input type="hidden" id="cookieDomain" value=".monster.com" />
<input type="hidden" id="searchPageAction" value="https://www.monster.com/jobs/search/" />
<input type="hidden" id="mcMainBox" class="mc-mail-box" value="" />
<input type="hidden" id="mcAwsUrl" value="" />

<input type="hidden" id="countryCode" value="US" />
<input type="hidden" id="languageCode" value="EN" />
<input type="hidden" id="typeAheadRequestUrl" value="https://c6v0t0t861.execute-api.us-east-1.amazonaws.com/Prod/vulcantypeaheadresource?matchString=%Q&amp;countrycode={0}&amp;languagecode={1}&amp;fuzziness=0" />
<input type="hidden" id="esTypeaheadEnabled" value="True" />
<input type="hidden" id="msgKeywords" value="Key Words" />
<input type="hidden" id="msgJobTitles" value="Job Titles" />
<input type="hidden" id="msgCompanyNames" value="Company Names" />

<div id="pv_nav-fixed">
    <!-- Top Nav -->
    <nav class="solid-nav navbar-2 navbar navbar-default navbar-fixed-top" role="navigation" id="jsrHeader">
        <div style="display: none" class="interMsgsW cookie-msg">
            <div class="interMsgsPar">
                <div class="interMsg">
                    <a onclick="return false;" name="closeIMEmployer" href="#" class="close-msg" title="Don&#39;t display this message again">
                        <span class="dontDisplay">Don&#39;t display this message again</span>
                        <span class="counter"></span><span class="fa fa-times"></span>
                    </a>
                    <h4>A Note About Cookies</h4>

                </div>
            </div>
        </div>
        <div class="container-fluid navbar-main">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <a class="navbar-brand" href="https://www.monster.com" aria-label="Monster Home">
                    <div class="logo">&nbsp;</div>
                </a>
                <!-- End Monster Logo -->
                <!-- Buttons in reverse order for Bootstrap -->
                <!-- New "Trigger" classes on buttons for JS (transitions.closeDropdowns()) -->
                <button type="button" class="navbar-toggle nav-trigger action action--open" aria-label="Open Menu">
                    <span class="sr-only">Toggle Navigation Mobile</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <!-- End Hamburger Button -->
                <button type="button" class="navbar-toggle navbar-toggle-account account-trigger action action--open-2 hidden-sm hidden-md hidden-lg" aria-label="Open Menu">
                    <span class="sr-only">Toggle Account Navigation</span>
                        <span class="navbar-profile-icon center-block"></span>
                    <span class="emailCount"></span>
                    <span class="logged-name">Account</span>
                </button>
                <!-- End Account Button -->
                <button type="button" class="navbar-toggle search-btn-container search-trigger" data-toggle="collapse" data-target="#mobile-navbar-search" aria-expanded="false">
                    <i class="fa fa-search"></i>
                    <span class="navbar-text">Jobs</span>
                </button>
                <!-- End Search Button -->
            </div>
            <!-- End Mobile Header/Navbar -->
            <div class="collapse navbar-collapse text-center" id="mobile-navbar-search" style="max-height: 423px;">
                <!-- End Navbar Right, Login, Signup, & Employer Links -->
                <form id="quickJobSearch" role="search" class="navbar-form" method="get">
                    <div class="form-group top-search keywords">
                        <label for="keywords" class="sr-only">Keywords</label>
                        <div class="input-group input-group-sm">
                            <span class="input-group-addon"><i class="zmdi zmdi-search"></i></span>
                                <div id="multiple-datasets">
                                    <input type="text" class="form-control typeaheadR tt-hint hasclear" placeholder="Search for Jobs" id="keywords2" name="q" value="Python" />
                                    <input type="hidden" id="typeaheadvalues" value="" />
                                </div>
                            <span class="input-clear" style="">x</span>
                        </div>
                    </div>
                    <div class="form-group top-search location">
                        <label for="location" class="sr-only">Location</label>
                        <div class="input-group input-group-sm">
                            <span class="input-group-addon"><i class="zmdi zmdi-pin"></i></span>
                            <input type="text" autocomplete="off" id="location" name="where" class="form-control input-sm typeahead hasclear" placeholder="Location" value="" />
                            <span class="input-clear" style="">x</span>
                        </div>
                    </div>
                    <button onclick="InitializeGlobalheaderSearch(); return false;" class="btn btn-white btn-sm" type="button" id="doQuickSearch">Search</button>
                        <div class="tm-wrap">
                            <input class="tm-input hidden" type="hidden" maxlength="200" />
                        </div>
                </form>

                <!-- End Search Form (Desktop & Mobile) -->
                <ul class="nav navbar-nav navbar-right hidden-xs">
                    <li class="dropdown account-dropdown">
                        <a href="#" class="dropdown-toggle navbar-icon-link loginLink2" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
                            <span class="sr-only">Toggle Account Navigation</span>
                                <span class="navbar-profile-icon center-block"></span>
                            <span class="emailCount"></span>
                            <span>Account</span>
                        </a>
                        <ul class="dropdown-menu">
                                <li>
                                    <a href="https://login20.monster.com/?r=https%3a%2f%2fwww.monster.com%2fjobs%2fsearch%2f%3fq%3dPython&amp;ch=MONS" title="Log In" gfltrack="1" >Log In</a>
                                </li>
                                <li>
                                    <a href="https://login20.monster.com/Become-Member/Create-Account?r=https%3a%2f%2fwww.monster.com%2fjobs%2fsearch%2f%3fq%3dPython&amp;landedFrom=Header&amp;ch=MONS" title="Sign Up" gfltrack="1" >Sign Up</a>
                                </li>
                        </ul>
                    </li>
                        <li>
                            <div id="login-btn-employer">
                                <a href="http://hiring.monster.com/?intcid=skr_LPF_TopNav_Employer" title="Employers: Post Jobs and Find Talent">
                                    Employers<br>
                                    <span>Post Jobs &amp; Find Talent </span>
                                </a>
                            </div>
                        </li>
                </ul>
            </div>
        </div>
        <div class="container-fluid subnav top-subnav hidden-xs">
            <ul class="nav navbar-nav hidden-xs subnav-nav clearfix">
                        <li id="main-nav-0" class="dropdown">
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
                                Find Jobs <span class="caret"></span>
                            </a>
                            <ul class="dropdown-menu">

            <li id="sub-nav-0">
                <a href="https://www.monster.com/jobs/advanced-search">Advanced Search</a>
            </li>
            <li id="sub-nav-1">
                <a href="https://www.monster.com/jobs/">Browse Jobs</a>
            </li>
<div class="cmsNavContainer componentDC1">
<h3 class="fnt5">Most Popular Jobs</h3>

<ul>
	<li><a href="https://www.monster.com/jobs/q-courier-jobs.aspx" title="Courier Jobsg">Courier Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-delivery-driver-jobs.aspx" title="Delivery Driver Jobs">Delivery Driver Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-dental-assistant-jobs.aspx" title="Dental Assistant Jobs">Dental Assistant Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-electrician-jobs.aspx" title="Electrician Jobs">Electrician Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-medical-assistant-jobs.aspx" title="Medical Assistant Jobs">Medical Assistant Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-truck-driver-jobs.aspx" title="Truck Driver Jobs">Truck Driver Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-pharmacist-jobs.aspx" title="Pharmacist Jobs">Pharmacist Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-pharmacy-technician-jobs.aspx" title="Pharmacy Technician Jobs">Pharmacy Technician Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-receptionist-jobs.aspx" title="Receptionist Jobs">Receptionist Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-security-guard-jobs.aspx" title="Security Guard Jobs">Security Guard Jobs</a></li>
</ul>
</div>

                            </ul>
                        </li>
                        <li id="main-nav-1" class="dropdown">
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
                                Career Resources <span class="caret"></span>
                            </a>
                            <ul class="dropdown-menu">

            <li id="sub-nav-2">
                <a href="https://www.monster.com/career-advice">Career Advice</a>
            </li>
            <li id="sub-nav-3">
                <a href="http://career-services.monster.com/">Career Services</a>
            </li>
            <li id="sub-nav-4">
                <a href="https://www.monster.com/communities">Communities</a>
            </li>
            <li id="sub-nav-5">
                <a href="https://www.monster.com/news">Employment News</a>
            </li>
<div class="cmsNavContainer componentDC2">
<h3 class="fnt5">Additional Resources</h3>

<ul>
	<li><a class="ext" href="https://www.topresume.com/resume-writing/?pt=eTBKg0FP8WHu&amp;por=monster&amp;utm_medium=referral&amp;utm_source=Monster+TopResume&amp;utm_content=Resume_CareerResources_RWS" title="Resume Writing Services">Resume Writing Services</a></li>
	<li><a class="ext" href="https://www.monster.com/career-advice/cover-letter-resume" title="Resume Advice">Resume Advice</a></li>
	<li><a class="ext" href="https://www.monster.com/career-advice/job-interview" title="Interviewing Tips
    ">Interviewing Tips</a></li>
	<li><a href="https://www.monster.com/personal-finance-center" title="Personal Finance Center">Personal Finance Center</a></li>
	<li><a href="https://www.monster.com/career-advice/salary-benefits" title="Salary &amp; Benefits">Salary &amp; Benefits</a></li>
	<li><a class="ext" href="https://www.monster.com/career-advice/article/industry-career-advice" title="Career Advice by Industry">Career Advice by Industry</a></li>
	<li><a href="https://www.monster.com/career-advice/professional-development/education-training" title="Education &amp; Training">Education &amp; Training</a></li>
	<li><a href="https://www.monster.com/blog" target="">Monster Blog</a></li>
	<li><a href="http://resources.monster.com/diversity-inclusion/work/" title="Diversity Resources">Diversity Resources</a></li>
</ul>
</div>

                            </ul>
                        </li>
                        <li id="main-nav-2">
                            <a href="https://www.monster.com/resumes/post-resume?landedFrom=Header">Post a Resume
</a>
                        </li>
                        <li id="main-nav-3">
                            <a href="https://www.monster.com/company">Company Profiles</a>
                        </li>
            </ul>

        </div>
        <!-- End Main Nav or "Subnav" (Desktop)-->
        <!-- Slideout Menu Container -->
        <div class="container">
            <!-- Menu -->
            <nav id="ml-menu-2" class="menu">
                <!-- Close button for mobile version -->
                <button class="action action--close-2" aria-label="Close Menu">×</button>
                <div class="menu__wrap">
                    <ul data-menu="main" class="menu__level menu__level--current">
                            <li class="menu__item">
                                <a class="menu__link" href="https://login20.monster.com/?r=https%3a%2f%2fwww.monster.com%2fjobs%2fsearch%2f%3fq%3dPython&amp;ch=MONS" title="Log In" gfltrack="1" >Log In</a>
                            </li>
                            <li class="menu__item">
                                <a class="menu__link" href="https://login20.monster.com/Become-Member/Create-Account?r=https%3a%2f%2fwww.monster.com%2fjobs%2fsearch%2f%3fq%3dPython&amp;landedFrom=Header&amp;ch=MONS" title="Sign Up" gfltrack="1" >Sign Up</a>
                            </li>
                    </ul>
                </div>
            </nav>
        </div>
        <!-- End Main Container for Mobile Main Nav -->
        <!-- Main container -->
        <div class="container">
            <!-- Menu -->
            <!-- Mobile Left Nav -->
            <nav id="ml-menu" class="menu">
                <!-- Close button for mobile version -->
                <button class="action action--close" aria-label="Close Menu">×</button>
                <!-- Edit contents of Init Crumb 1 to edit first breadcrumb in left slidout menu. -->
                <span id="init-crumb-1" style="display: none; visibility: hidden;">all</span>
                <!-- Menu contents. -->
                <div id="ml-menu-container" class="menu__wrap">
                    <ul data-menu="main" class="menu__level menu__level--current">
                        <li id="mobile-nav-home" class="menu__item">
                                <a class="menu__link" href="https://www.monster.com">Home</a>
                        </li>
                                <li id="mobile-nav-0" class="menu__item">
                                    <a class="menu__link" data-submenu="submenu-0" href="#">Find Jobs</a>
                                    <ul data-menu="submenu-0" class="menu__level">

    <li id="mobile-subnav-0" class="menu__item">
        <a class="menu__link" href="https://www.monster.com/jobs/advanced-search">Advanced Search</a>
    </li>
    <li id="mobile-subnav-1" class="menu__item">
        <a class="menu__link" href="https://www.monster.com/jobs/">Browse Jobs</a>
    </li>
    <li id="mobile-subnav-" class="menu__item">
        <a class="menu__link" data-submenu="submenu-cms-109" href="#"></a>
        <ul data-menu="submenu-cms-109" data-sub-for="109" class="menu__level cms-submenu">
            <div class="cmsNavContainer componentDC1">
<h3 class="fnt5">Most Popular Jobs</h3>

<ul>
	<li><a href="https://www.monster.com/jobs/q-courier-jobs.aspx" title="Courier Jobsg">Courier Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-delivery-driver-jobs.aspx" title="Delivery Driver Jobs">Delivery Driver Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-dental-assistant-jobs.aspx" title="Dental Assistant Jobs">Dental Assistant Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-electrician-jobs.aspx" title="Electrician Jobs">Electrician Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-medical-assistant-jobs.aspx" title="Medical Assistant Jobs">Medical Assistant Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-truck-driver-jobs.aspx" title="Truck Driver Jobs">Truck Driver Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-pharmacist-jobs.aspx" title="Pharmacist Jobs">Pharmacist Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-pharmacy-technician-jobs.aspx" title="Pharmacy Technician Jobs">Pharmacy Technician Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-receptionist-jobs.aspx" title="Receptionist Jobs">Receptionist Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-security-guard-jobs.aspx" title="Security Guard Jobs">Security Guard Jobs</a></li>
</ul>
</div>

        </ul>
    </li>

                                    </ul>
                                </li>
                                <li id="mobile-nav-1" class="menu__item">
                                    <a class="menu__link" data-submenu="submenu-1" href="#">Career Resources</a>
                                    <ul data-menu="submenu-1" class="menu__level">

    <li id="mobile-subnav-2" class="menu__item">
        <a class="menu__link" href="https://www.monster.com/career-advice">Career Advice</a>
    </li>
    <li id="mobile-subnav-3" class="menu__item">
        <a class="menu__link" href="http://career-services.monster.com/">Career Services</a>
    </li>
    <li id="mobile-subnav-4" class="menu__item">
        <a class="menu__link" href="https://www.monster.com/communities">Communities</a>
    </li>
    <li id="mobile-subnav-5" class="menu__item">
        <a class="menu__link" href="https://www.monster.com/news">Employment News</a>
    </li>
    <li id="mobile-subnav-" class="menu__item">
        <a class="menu__link" data-submenu="submenu-cms-165" href="#"></a>
        <ul data-menu="submenu-cms-165" data-sub-for="165" class="menu__level cms-submenu">
            <div class="cmsNavContainer componentDC2">
<h3 class="fnt5">Additional Resources</h3>

<ul>
	<li><a class="ext" href="https://www.topresume.com/resume-writing/?pt=eTBKg0FP8WHu&amp;por=monster&amp;utm_medium=referral&amp;utm_source=Monster+TopResume&amp;utm_content=Resume_CareerResources_RWS" title="Resume Writing Services">Resume Writing Services</a></li>
	<li><a class="ext" href="https://www.monster.com/career-advice/cover-letter-resume" title="Resume Advice">Resume Advice</a></li>
	<li><a class="ext" href="https://www.monster.com/career-advice/job-interview" title="Interviewing Tips
    ">Interviewing Tips</a></li>
	<li><a href="https://www.monster.com/personal-finance-center" title="Personal Finance Center">Personal Finance Center</a></li>
	<li><a href="https://www.monster.com/career-advice/salary-benefits" title="Salary &amp; Benefits">Salary &amp; Benefits</a></li>
	<li><a class="ext" href="https://www.monster.com/career-advice/article/industry-career-advice" title="Career Advice by Industry">Career Advice by Industry</a></li>
	<li><a href="https://www.monster.com/career-advice/professional-development/education-training" title="Education &amp; Training">Education &amp; Training</a></li>
	<li><a href="https://www.monster.com/blog" target="">Monster Blog</a></li>
	<li><a href="http://resources.monster.com/diversity-inclusion/work/" title="Diversity Resources">Diversity Resources</a></li>
</ul>
</div>

        </ul>
    </li>

                                    </ul>
                                </li>
                                <li id="mobile-nav-2" class="menu__item">
                                    <a class="menu__link" href="https://www.monster.com/resumes/post-resume?landedFrom=Header">Post a Resume
</a>
                                </li>
                                <li id="mobile-nav-3" class="menu__item">
                                    <a class="menu__link" href="https://www.monster.com/company">Company Profiles</a>
                                </li>


                    </ul>
                </div>
            </nav>
        </div>
        <!-- End Main Container for Mobile Main Nav -->

    </nav>
    <!-- End Navbar Fixed Top -->

    <!-- Nav Modal End -->
</div>




<script type="text/javascript">

    $(function () {
        //Sub-Menu Mobile
        var $mlSubMenus = $('#ml-menu-container ul[data-menu*="submenu-"]');
        if ($mlSubMenus.length) {
            $mlSubMenus.each(function () {
                $(this).appendTo('#ml-menu-container');
            });
        }

        //CMS Desktop
        var $cmsNavContainers = $("li[id*='main-nav-'] div.cmsNavContainer");
        if ($cmsNavContainers.length) {
            for (var i = 0; i < $cmsNavContainers.length; i++) {
                var $this = $($cmsNavContainers[i]);
                $this.addClass('hidden');
                var title = $this.find('h3').html();
                var $childs = $this.find('ul li');

                var $parentUl = $this.closest('ul');
                $parentUl.append('<li class="cmsNavContainer dropdown-sub"></li>');
                var $newCmsContainer = $parentUl.find('li.cmsNavContainer.dropdown-sub');
                $newCmsContainer.append('<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">' + title + ' <span class="caret"></span></a>');
                $newCmsContainer.append('<ul class="dropdown-menu dropdown-menu-sub"></ul>');
                $newCmsContainer.find('ul').append($childs);

                $this.remove();
            }
        }

        //CMS Mobile
        var $mobileCmsNavContainers = $("#ml-menu-container ul.cms-submenu div.cmsNavContainer");
        if ($mobileCmsNavContainers.length) {
            for (var i = 0; i < $mobileCmsNavContainers.length; i++) {
                var $this = $($mobileCmsNavContainers[i]);
                var $parentUl = $this.closest('ul.cms-submenu');

                $this.addClass('hidden');
                var thisTitle = $this.find('h3').html();
                var $thisChilds = $this.find('ul li');

                var dataMenu = $parentUl.attr('data-menu');
                var dataSubFor = $parentUl.attr('data-sub-for');

                $thisChilds.each(function () {
                    $(this).addClass('menu__item');
                    $(this).find('a').addClass('menu__link');
                });

                $thisChilds.appendTo($parentUl);
                $this.remove();

                var $subLinkAnchor = $("#ml-menu-container a.menu__link[data-submenu='submenu-cms-" + dataSubFor + "']");
                if ($subLinkAnchor.length) {
                    $subLinkAnchor.html(thisTitle);
                }
            }
        }

        setTimeout(function () {
            globalHeaderNavigation({"InitialBreadcrumbText":"all"});
        }, 300);
    });

    $(document).ready(function () {
        var isUsingAppDomainForServices = false;
        if ('False' === 'True') {
            isUsingAppDomainForServices = true;
        }

        InitializeHeaderBarJsr(isUsingAppDomainForServices); // all header related script
    });
</script>


    </div>


    <div class="wrap jsrMain">
	    <div class="content" id="jsr">
  		    <span class="anchor" id="mainContent"></span>
	        <div class="mainbar">
	            <div class="matter">



<style>
    .containerdebug .contentdebug {
        padding : 5px;
        background-color: #f7e7bd;
    }
    .containerdebug {
        border:1px solid #748649;
        word-wrap: break-word;
        padding: 0;
    }
    .containerdebug div {
        width:100%;
    }
    .containerdebug .headerdebug {
        background-color:#d3d3d3;
        padding: 2px;
        cursor: pointer;
        font-weight: bold;
    }
</style>





	                <!-- Main content starts -->
	                <div class="container">

    <div class="row">


    </div>
    <div class="row">
        <div class="col-sm-4 col-lg-3 hidden-xs jsr-left-rail" xmlns:ms="urn:schemas-microsoft-com:xslt" xmlns:ContentBlockManager="urn:content-block-manager" xmlns:WidgetManager="urn:widget-manager" xmlns:FormatUtils="urn:format-utils">


<input type="hidden" id="isDynamicResult" value="True" />

<input type="hidden" id="showNewJobs" value="False" />
<input type="hidden" id="enableNewJobsCount" value="False" />
<input type="hidden" id="lpfUrl" value="https://www.monster.com/jobs" />

<script type="text/javascript">
    $(document).ready(function () {

        InitializeNewJobsCount();

        $('[data-toggle="tooltip"]').tooltip();

        $('.jsr-left-rail .recent-searches-container .label').hover(function () {
            $(this).addClass('show-details');
        });

        $('.jsr-left-rail .recent-searches-container .label').mouseleave(function () {
            $(this).removeClass('show-details');
        });
    });
</script><div class="filterHeader">Filter Results By:</div>
<div class="refine">



     <div class="refine-section">
        <h4>Sort By:</h4>
        <div class="btn-group" role="group">
            <button class="btn btn-default sort-by-btn active" type="button"  onclick="setGetParameter('sort', 'rv.dt.di'); triggerFilterClick(null, 'sort', 'rv.dt.di');">Relevance</button>
            <button class="btn btn-default sort-by-btn " type="button" onclick="setGetParameter('sort', 'dt.rv.di'); triggerFilterClick(null, 'sort', 'dt.rv.di');">Date</button>
        </div>
    </div>
    <script type="text/javascript">
        $(document).ready(function () {
            $("button[class^='btn btn-default sort-by-btn']").on('click', function () {
                $(this).addClass('active');
            });
        });
    </script>

    <div class="refine-section">
        <h4>Company Search:</h4>
        <div class="form-group">
            <label class="sr-only" for="coSearch">Company Search</label>
            <input class="form-control" placeholder="Enter company name" aria-label="Company Search:" id="coSearch">
            <input id="companySearchUrl" type="hidden" value="https://www.monster.com/jobs/search/ZZcompanySearchZZ_6?q=Python">
        </div>
    </div>
    <script type="text/javascript">
        $(function () {
            InitializeCompanySearch();
        });
    </script>

<input type="hidden" id="evar63Json" value='{&quot;company&quot;: [&quot;&quot;],&quot;category&quot;: [&quot;&quot;],&quot;kywdjobtitle&quot;: [&quot;Python&quot;],&quot;location&quot;: [&quot;&quot;],&quot;skill&quot;: [&quot;&quot;],&quot;jobstatus&quot;: [&quot;&quot;],&quot;radius&quot;: [&quot;&quot;],&quot;sort&quot;: [&quot;&quot;]}' />

     <div class="refine-section">
         <h4>Job Status:</h4>
         <ul class="list">
                <li class="list__item">
                    <label class="label--checkbox">
                        <input type="checkbox" class="checkbox" disabled="disabled"    onclick="checkboxActionJobStatus(this, 'jobstatus', 'Full Time', 'https://www.monster.com/jobs/search/Full-Time_8?q=Python',  '')"/>
                        <span class="label--checkbox--span">Full Time</span>
                    </label>
                </li>
                <li class="list__item">
                    <label class="label--checkbox">
                        <input type="checkbox" class="checkbox" disabled="disabled"    onclick="checkboxActionJobStatus(this, 'jobstatus', 'Part Time', 'https://www.monster.com/jobs/search/Part-Time_8?q=Python',  '')"/>
                        <span class="label--checkbox--span">Part Time</span>
                    </label>
                </li>

         </ul>
    </div>
<script type="text/javascript">
       $("input.checkbox").removeAttr("disabled");

 </script>

</div>


    <div class="span3 menucontainer">
        <ul class="nav">
                            <li id="backlinkingwidgetSkill">
                                <h4>Skills:</h4>
                                <ul data-facettype="ft6" data-facetsearchparam="ftsp6" id="catdiv6" class="nav submenu" style="display: block;" aria-label="Skills:">
                                        <li onclick="triggerFilterClick(this, 'skill')"><a href="https://www.monster.com/jobs/search/?q=Python&amp;kwdv=1105" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Python Programming/Scripting Language">Python Programming/Scripting Language</a></li>
                                        <li onclick="triggerFilterClick(this, 'skill')"><a href="https://www.monster.com/jobs/search/?q=Python&amp;kwdv=713" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Java">Java</a></li>
                                        <li onclick="triggerFilterClick(this, 'skill')"><a href="https://www.monster.com/jobs/search/?q=Python&amp;kwdv=1075" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Scripting (Scripting Languages)">Scripting (Scripting Languages)</a></li>
                                        <li onclick="triggerFilterClick(this, 'skill')"><a href="https://www.monster.com/jobs/search/?q=Python&amp;kwdv=303" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Software Engineering">Software Engineering</a></li>
                                        <li onclick="triggerFilterClick(this, 'skill')"><a href="https://www.monster.com/jobs/search/?q=Python&amp;kwdv=1860" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Linux Operating System">Linux Operating System</a></li>
                                        <li id="showmoreSkillButton" class="showmorebutton">
                                            <a onclick="$('#showmoreSkillButton').hide();$('.showmoreSkillLinks').show();$('#showlessSkillButton').show();">Show More <span class="mdi mdi-chevron-down"></span></a>
                                        </li>
                                                <li onclick="triggerFilterClick(this, 'skill')" class="showmoreSkillLinks"><a href="https://www.monster.com/jobs/search/?q=Python&amp;kwdv=2014" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Perl Programming Language">Perl Programming Language</a></li>
                                                <li onclick="triggerFilterClick(this, 'skill')" class="showmoreSkillLinks"><a href="https://www.monster.com/jobs/search/?q=Python&amp;kwdv=1163" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="C++ Programming Language">C++ Programming Language</a></li>
                                                <li onclick="triggerFilterClick(this, 'skill')" class="showmoreSkillLinks"><a href="https://www.monster.com/jobs/search/?q=Python&amp;kwdv=1158" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="C Programming Language">C Programming Language</a></li>
                                                <li onclick="triggerFilterClick(this, 'skill')" class="showmoreSkillLinks"><a href="https://www.monster.com/jobs/search/?q=Python&amp;kwdv=1072" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="SQL (Structured Query Language)">SQL (Structured Query Language)</a></li>
                                                <li onclick="triggerFilterClick(this, 'skill')" class="showmoreSkillLinks"><a href="https://www.monster.com/jobs/search/?q=Python&amp;kwdv=2193" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="JavaScript">JavaScript</a></li>
                                        <li id="showlessSkillButton" class="showlessButton">
                                            <a onclick="$('#showlessSkillButton').hide();$('.showmoreSkillLinks').hide();$('#showmoreSkillButton').show();">Show Less <span class="mdi mdi-chevron-up"></span></a>
                                        </li>
                                </ul>
                            </li>
                            <li id="backlinkingwidgetCity">
                                <h4>City:</h4>
                                <ul data-facettype="ft2" data-facetsearchparam="ftsp2" id="catdiv2" class="nav submenu" style="display: block;" aria-label="City:">
                                        <li onclick="triggerFilterClick(this, 'location')"><a href="https://www.monster.com/jobs/search/?q=Python&amp;where=New-York__2c-NY" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL City Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="New York, NY">New York</a></li>
                                        <li onclick="triggerFilterClick(this, 'location')"><a href="https://www.monster.com/jobs/search/?q=Python&amp;where=Seattle__2c-WA" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL City Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Seattle, WA">Seattle</a></li>
                                        <li onclick="triggerFilterClick(this, 'location')"><a href="https://www.monster.com/jobs/search/?q=Python&amp;where=San-Francisco__2c-CA" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL City Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="San Francisco, CA">San Francisco</a></li>
                                        <li onclick="triggerFilterClick(this, 'location')"><a href="https://www.monster.com/jobs/search/?q=Python&amp;where=Santa-Clara__2c-CA" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL City Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Santa Clara, CA">Santa Clara</a></li>
                                        <li onclick="triggerFilterClick(this, 'location')"><a href="https://www.monster.com/jobs/search/?q=Python&amp;where=Chicago__2c-IL" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL City Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Chicago, IL">Chicago</a></li>
                                        <li id="showmoreCityButton" class="showmorebutton">
                                            <a onclick="$('#showmoreCityButton').hide();$('.showmoreCityLinks').show();$('#showlessCityButton').show();dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL City Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});">Show More <span class="mdi mdi-chevron-down"></span></a>
                                        </li>
                                                <li onclick="triggerFilterClick(this, 'location')" class="showmoreCityLinks"><a href="https://www.monster.com/jobs/search/?q=Python&amp;where=San-Diego__2c-CA" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL City Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="San Diego, CA">San Diego</a></li>
                                                <li onclick="triggerFilterClick(this, 'location')" class="showmoreCityLinks"><a href="https://www.monster.com/jobs/search/?q=Python&amp;where=San-Jose__2c-CA" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL City Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="San Jose, CA">San Jose</a></li>
                                                <li onclick="triggerFilterClick(this, 'location')" class="showmoreCityLinks"><a href="https://www.monster.com/jobs/search/?q=Python&amp;where=Austin__2c-TX" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL City Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Austin, TX">Austin</a></li>
                                                <li onclick="triggerFilterClick(this, 'location')" class="showmoreCityLinks"><a href="https://www.monster.com/jobs/search/?q=Python&amp;where=Sunnyvale__2c-CA" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL City Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Sunnyvale, CA">Sunnyvale</a></li>
                                                <li onclick="triggerFilterClick(this, 'location')" class="showmoreCityLinks"><a href="https://www.monster.com/jobs/search/?q=Python&amp;where=Palo-Alto__2c-CA" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL City Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Palo Alto, CA">Palo Alto</a></li>
                                        <li id="showlessCityButton" class="showlessButton">
                                            <a onclick="$('#showlessCityButton').hide();$('.showmoreCityLinks').hide();$('#showmoreCityButton').show();">Show Less <span class="mdi mdi-chevron-up"></span></a>
                                        </li>
                                </ul>
                            </li>
        </ul>
    </div>
    <br />
            <div class="refine similar-jobtitle">
                <div class="refine-section">
                    <h4>Related Job Titles:</h4>
                    <ul aria-label="Related Job Titles:">
                            <li onclick="triggerFilterClick(this, 'kywdjobtitle')">
                                <span class="label label-default refinement-tag">
                                    <span class="refinement-tag-text"><a href="https://www.monster.com/jobs/search/Software-Engineer_5" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Software Engineer">Software Engineer</a></span>
                                </span>
                            </li>
                            <li onclick="triggerFilterClick(this, 'kywdjobtitle')">
                                <span class="label label-default refinement-tag">
                                    <span class="refinement-tag-text"><a href="https://www.monster.com/jobs/search/Data-Scientist_5" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Data Scientist">Data Scientist</a></span>
                                </span>
                            </li>
                            <li onclick="triggerFilterClick(this, 'kywdjobtitle')">
                                <span class="label label-default refinement-tag">
                                    <span class="refinement-tag-text"><a href="https://www.monster.com/jobs/search/DevOps-Engineer_5" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="DevOps Engineer">DevOps Engineer</a></span>
                                </span>
                            </li>
                            <li onclick="triggerFilterClick(this, 'kywdjobtitle')">
                                <span class="label label-default refinement-tag">
                                    <span class="refinement-tag-text"><a href="https://www.monster.com/jobs/search/Quality-Assurance-Engineer_5" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Quality Assurance Engineer">Quality Assurance Engineer</a></span>
                                </span>
                            </li>
                            <li onclick="triggerFilterClick(this, 'kywdjobtitle')">
                                <span class="label label-default refinement-tag">
                                    <span class="refinement-tag-text"><a href="https://www.monster.com/jobs/search/Cloud-Computing-Engineer_5" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Cloud Computing Engineer">Cloud Computing Engineer</a></span>
                                </span>
                            </li>
                    </ul>
                </div>
            </div>
        <script type="text/javascript">
          //  $(document).ready(function () {
                $('.showmoreStateLinks').hide();
                $('.showmoreCityLinks').hide();
                $('.showmoreCompanyLinks').hide();
                $('.showmoreVerticalLinks').hide();
                $('.showmoreJobTitleLinks').hide();
                $('.showmoreSkillLinks').hide();
          //  });
        </script>


        </div>
        <div class="col-sm-8 col-lg-7 jsr-mid" xmlns:formatutils="urn:format-utils" xmlns:widgetmanager="urn:widget-manager" xmlns:contentblockmanager="urn:content-block-manager" xmlns:ms="urn:schemas-microsoft-com:xslt">
            <div class="row" id="main">
                <div class="col-xs-12 jsresultsheader">

    <div class="visible-xs" id="mobileEmailWidget">

<input type="hidden" id="searchQuery" value="q=Python&amp;brd=1&amp;brd=2&amp;cy=US&amp;pp=25&amp;sort=rv.di.dt&amp;stp=TwoBoxBand" />
<input type="hidden" id="isLoggedIn" value="false" />
<input type="hidden" id="maxSaveSearchesAllowed" value="5" />
<input type="hidden" id="emailUrl" value="https://www.monster.com/jobs/emailjobs?q=Python" />
<input type="hidden" id="isDynamicPage" value="True" />

        <div class="jobAlertButton">
            <button type="submit" id="emailButton3" class="emailButton">Email me Jobs</button>
        </div>
      <div class="jobAlerts">

            <span class="jobAlert_Close" aria-label="Close" title="Close">X</span>
            <div class="marked-title clearfix">
                <h3><i class="fa fa-envelope"></i> Get jobs by email for this search</h3>
            </div>
            <div class="row">
                <div class="col-xs-12 col-sm-7 col-md-7">
                    <label class="sr-only" for="emailAddress">Enter Your Email Address</label>
                    <input type="text" placeholder="Enter Your Email Address" id="emailAddress1" name="emailAddress1" value="" class="form-control">
                </div>
                <div class="col-xs-12 col-sm-5 col-md-5">
                    <button data-loading-text="<i class='fa fa-spinner fa-spin'></i>" type="button" id="emailButton2" value="Email Me Jobs " title="Email me Jobs " onclick="dataLayer.push({'eventCategory':'Sidebar Widgets','eventAction':'JSA','eventLabel':'Click Link in Widget'});; emailActionMobileClick(this); ">
                        Email Me Jobs
                    </button>
                </div>
            </div>
            <div class="messageholder">
            </div>
            <div class="litRegPrivacy fnt1" runat="server" id="privacyMSG" visible="False">
                 By continuing you agree to Monster's <a title="privacy policy" target="_blank" href="http://my.monster.com/Privacy/Default.aspx">Privacy Policy</a>, <a title="terms of use" target="_blank" href="http://my.monster.com/Terms/Default.aspx">Terms of Use</a> and <a title="use of cookies" target="_blank" href="http://inside.monster.com/cookie-info/inside2.aspx">Use of Cookies</a>.
            </div>
         </div>



<script type="text/javascript">

    $(function() {
        setUpScroll();


        var isLoggedin = false;
        if (isLoggedin) {
            var emailAddr = getParameterByName('addr');
            var searchQuery =  $('#searchQuery').val();
            if (emailAddr && searchQuery) {
                dataLayer.push({'eventCategory':'Sidebar Widgets','eventAction':'JSA','eventLabel':'Click Link in Widget'});;
                emailAction(emailAddr, searchQuery);
             }
         }
    });

</script>




    </div>


<h1>
         Python Jobs
</h1>



<h2 class="page-title hidden-xs">
    1000+ Jobs Found
</h2>
<h2 class="page-title visible-xs">
    1000+ Jobs Found
</h2>
                </div>


                <div class="col-xs-12">


<script type="application/ld+json">

            {"@context":"https://schema.org","@type":"ItemList","mainEntityOfPage":{
            "@type":"CollectionPage","@id":"https://www.monster.com/jobs/search/?q=Python"
            }
            ,"itemListElement":[

                 {"@type":"ListItem","position":1,"url":"http://jobview.monster.com/principal-python-engineer-python-java-django-up-to-180k-job-sausalito-ca-us-182877962.aspx"}
                    ,
                 {"@type":"ListItem","position":2,"url":"http://jobview.monster.com/python-django-job-us-182712122.aspx"}
                    ,
                 {"@type":"ListItem","position":3,"url":"http://jobview.monster.com/senior-python-django-developer-job-san-francisco-ca-us-182548380.aspx"}
                    ,
                 {"@type":"ListItem","position":4,"url":"http://jobview.monster.com/python-java-django-developer-job-east-hartford-ct-us-182475182.aspx"}
                    ,
                 {"@type":"ListItem","position":5,"url":"http://jobview.monster.com/python-django-developers-wanted-job-arlington-va-us-181233697.aspx"}
                    ,
                 {"@type":"ListItem","position":6,"url":"http://jobview.monster.com/python-django-developer-job-washington-dc-us-183173717.aspx"}
                    ,
                 {"@type":"ListItem","position":7,"url":"http://jobview.monster.com/seeking-a-python-javascript-full-stack-engineer-in-mountain-view-ca-job-mountain-view-ca-us-179114121.aspx"}
                    ,
                 {"@type":"ListItem","position":8,"url":"http://jobview.monster.com/developer-python-django-job-washington-dc-dc-us-182907351.aspx"}
                    ,
                 {"@type":"ListItem","position":9,"url":"http://job-openings.monster.com/monster/b9199795-dcba-49d2-abf3-9cba2f412481"}
                    ,
                 {"@type":"ListItem","position":10,"url":"http://jobview.monster.com/python-developer-job-new-york-ny-us-182696971.aspx"}
                    ,
                 {"@type":"ListItem","position":11,"url":"http://jobview.monster.com/python-developer-job-blue-hills-ct-us-182997939.aspx"}
                    ,
                 {"@type":"ListItem","position":12,"url":"http://jobview.monster.com/senior-python-developer-job-seattle-wa-us-182989858.aspx"}
                    ,
                 {"@type":"ListItem","position":13,"url":"http://jobview.monster.com/cloud-python-developer-job-princeton-township-nj-us-181672808.aspx"}
                    ,
                 {"@type":"ListItem","position":14,"url":"http://jobview.monster.com/python-developer-job-san-jose-ca-us-182931848.aspx"}
                    ,
                 {"@type":"ListItem","position":15,"url":"http://jobview.monster.com/full-stack-python-engineer-job-cary-nc-us-182287507.aspx"}
                    ,
                 {"@type":"ListItem","position":16,"url":"http://jobview.monster.com/python-developer-job-seattle-wa-us-182601362.aspx"}
                    ,
                 {"@type":"ListItem","position":17,"url":"http://jobview.monster.com/sr-python-developer-job-floral-park-ny-us-181055025.aspx"}
                    ,
                 {"@type":"ListItem","position":18,"url":"http://jobview.monster.com/python-developer-6-12-months-contract-job-chicago-il-us-182072378.aspx"}
                    ,
                 {"@type":"ListItem","position":19,"url":"http://jobview.monster.com/python-engineer-job-san-francisco-ca-us-182493103.aspx"}
                    ,
                 {"@type":"ListItem","position":20,"url":"http://jobview.monster.com/python-engineer-consultant-ii-job-san-jose-ca-us-182394144.aspx"}
                    ,
                 {"@type":"ListItem","position":21,"url":"http://jobview.monster.com/python-developer-job-mountain-view-ca-us-183183020.aspx"}
                    ,
                 {"@type":"ListItem","position":22,"url":"http://jobview.monster.com/jr-python-or-scala-developer-job-south-plainfield-nj-us-171837225.aspx"}
                    ,
                 {"@type":"ListItem","position":23,"url":"http://jobview.monster.com/python-developer-job-new-york-city-ny-us-182825475.aspx"}
                    ,
                 {"@type":"ListItem","position":24,"url":"http://jobview.monster.com/python-developer-job-hillsboro-or-us-182773102.aspx"}
                    ,
                 {"@type":"ListItem","position":25,"url":"http://jobview.monster.com/sdet-java-python-job-seattle-wa-us-182746774.aspx"}
            ]}


</script>
    <section id="resultsWrapper">
                    <div class="js_result_container featured-ad clearfix">
                        <script language="javaScript" type="text/javascript" id="AdScript_Middle_FeaturedEmployer" name="AdScript_Middle_FeaturedEmployer">
	var OAS_RNS = 028637960;
                                                        var OAS_taxonomy='site=mons&affiliate=mons&app=js&size=0x112&oas_pv=no_analytics&key=python&fb=0&cy=US&sapp=jsr&app=js';
                                                        var OAS_query='site=mons&affiliate=mons&app=js&size=0x112&oas_pv=no_analytics&key=python&fb=0&cy=US&sapp=jsr&app=js';
	                                                    OAS_query == '' ? OAS_query+='XE' + '&' + OAS_taxonomy + OAS_rdl + "&if_nt_CookieAccept=" + OAS_CA + '&XE': OAS_query+= '&XE' + '&' + OAS_taxonomy + OAS_rdl + "&if_nt_CookieAccept=" + OAS_CA + '&XE';
	                                                    document.write('<iframe width=100% height=112 id=AdFrame_Middle_FeaturedEmployer name=AdFrame_Middle_FeaturedEmployer class="" marginwidth=0 marginheight=0 hspace=0 vspace=0 frameborder=0 scrolling=no bordercolor="#000000" src="https://oas.monster.com/RealMedia/ads/adstream_sx.ads/us.monster.en/jsrnew/powersearch.aspx/1' + OAS_RNS + '@Middle,BottomRight,Left1,Left2,Middle1,Left3,Right3,Right,Right1,Right2,x42,x18,Bottom1,Top,TopRight!Middle?' + OAS_query + '" title="Advertisement"></iframe>');

</script>
                    </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xcyberc3x" data-m_impr_j_jawsid="229297753" data-m_impr_j_jobid="182877962" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="37.8489" data-m_impr_j_lid="20586" data-m_impr_j_long="-122.4964" data-m_impr_j_occid="11970" data-m_impr_j_p="1" data-m_impr_j_postingid="4c58fca6-dd6f-4e0c-a191-dd9e7ac66b59" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="3732fc9a-ee95-47c1-86f8-75644db3e1ce" href="http://jobview.monster.com/principal-python-engineer-python-java-django-up-to-180k-job-sausalito-ca-us-182877962.aspx?mescoid=1500127001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;1&#39;});; clickJobTitle(&#39;plid=20586&amp;pcid=660&amp;poccid=11970&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Principal Python Engineer - Python, Java, Django up to 180K&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xcyberc3x_CyberCoders&quot;,&quot;eVar31&quot;:&quot;Sausalito_CA_94965&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-06T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Principal Python Engineer - Python, Java, Django up to 180K"><span itemprop="title">Principal Python Engineer - Python, Java, Django up to 180K</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-cybercoders.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;1&#39;});" title="CyberCoders"><span itemprop="name">CyberCoders</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-california.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;1&#39;});" title="Sausalito, CA, 94965"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Sausalito, CA
            <meta itemprop="addressLocality" content="Sausalito" />
            <meta itemprop="addressRegion" content="CA" />
            <meta itemprop="postalCode" content="94965" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-06T12:00" itemprop="datePosted">14 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="If you are a Principal Python Engineer with experience doing senior level Python development for web based applications, please read on!

We&#39;re a well-funded startup Headquartered right across the iconic Golden Gate Bridge in Marin County! Our platf......" />
                    <meta itemprop="url" content="http://jobview.monster.com/principal-python-engineer-python-java-django-up-to-180k-job-sausalito-ca-us-182877962.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xw150616192wx" data-m_impr_j_jawsid="228530877" data-m_impr_j_jobid="182712122" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="0" data-m_impr_j_lid="323" data-m_impr_j_long="0" data-m_impr_j_occid="11970" data-m_impr_j_p="2" data-m_impr_j_postingid="54e0a0b1-8bdd-412b-a7f3-328c5ce60c3b" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="4c46addb-df7a-49ea-92e4-e74465c84d0b" href="http://jobview.monster.com/python-django-job-us-182712122.aspx?mescoid=9901111000004&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;2&#39;});; clickJobTitle(&#39;plid=323&amp;pcid=660&amp;poccid=11970&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;PYTHON/DJANGO&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xw150616192wx_W3Global, Inc&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-06T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="PYTHON/DJANGO"><span itemprop="title">PYTHON/DJANGO</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-w3global__2c-inc.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;2&#39;});" rel="nofollow" title="W3Global, Inc"><span itemprop="name">W3Global, Inc</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">

        <meta itemprop="name" content="" />
</span>
                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-06T12:00" itemprop="datePosted">14 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Position- Python/Django Job Location- Remote Option Job Type- Full Time



Requirements

Excellent Python/Django development skills

Understanding of software engineering cycles, principles, and versioning

Experience with bug-tracker software
......" />
                    <meta itemprop="url" content="http://jobview.monster.com/python-django-job-us-182712122.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xhnusx" data-m_impr_j_jawsid="227815969" data-m_impr_j_jobid="182548380" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="47.6157" data-m_impr_j_lid="355" data-m_impr_j_long="-122.3445" data-m_impr_j_occid="11969" data-m_impr_j_p="3" data-m_impr_j_postingid="3ba94ee6-bc20-4116-b663-10f28044cacc" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="542730dc-336c-4759-8b0b-4819d541a0d5" href="http://jobview.monster.com/senior-python-django-developer-job-san-francisco-ca-us-182548380.aspx?mescoid=1500129001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;3&#39;});; clickJobTitle(&#39;plid=355&amp;pcid=660&amp;poccid=11969&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Senior Python/Django Developer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xhnusx_Harvey Nash USA&quot;,&quot;eVar31&quot;:&quot;San Francisco_CA_98121&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-03T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Senior Python/Django Developer"><span itemprop="title">Senior Python/Django Developer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-harvey-nash.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;3&#39;});" title="Harvey Nash USA"><span itemprop="name">Harvey Nash USA</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-san-francisco,-ca.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;3&#39;});" title="San Francisco, CA, 98121"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    San Francisco, CA
            <meta itemprop="addressLocality" content="San Francisco" />
            <meta itemprop="addressRegion" content="CA" />
            <meta itemprop="postalCode" content="98121" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-03T12:00" itemprop="datePosted">17 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Are you a senior Python/Django engineer who would love to take on bigger challenges? Have you thought about working for an exciting start-up company in the heart of Seattle? Do you have what it takes to be an SME and build things from scratch? Then ......" />
                    <meta itemprop="url" content="http://jobview.monster.com/senior-python-django-developer-job-san-francisco-ca-us-182548380.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xeitprofesinx" data-m_impr_j_jawsid="227199552" data-m_impr_j_jobid="182475182" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="41.781" data-m_impr_j_lid="368" data-m_impr_j_long="-72.6206" data-m_impr_j_occid="11904" data-m_impr_j_p="4" data-m_impr_j_postingid="9281fdc1-1ad1-43de-95ca-f5e2391834a6" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="29e103d1-a3b5-4656-8bf9-665ece553f80" href="http://jobview.monster.com/python-java-django-developer-job-east-hartford-ct-us-182475182.aspx?mescoid=1500129001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;4&#39;});; clickJobTitle(&#39;plid=368&amp;pcid=660&amp;poccid=11904&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Python/JAVA/Django Developer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xeitprofesinx_E-IT Professionals India Private Limited&quot;,&quot;eVar31&quot;:&quot;East Hartford_CT_06108&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-03-31T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Python/JAVA/Django Developer"><span itemprop="title">Python/JAVA/Django Developer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-e__2dit-professionals-india-private-limited.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;4&#39;});" rel="nofollow" title="E-IT Professionals India Private Limited"><span itemprop="name">E-IT Professionals India Private Limited</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-east-hartford,-ct.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;4&#39;});" title="East Hartford, CT, 06108"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    East Hartford, CT
            <meta itemprop="addressLocality" content="East Hartford" />
            <meta itemprop="addressRegion" content="CT" />
            <meta itemprop="postalCode" content="06108" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-03-31T12:00" itemprop="datePosted">20 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="We have an Python/JAVA/Django Developer in East Hartford, CT. If you are interested kindly reply back with updated resume to  or call 734-821-3489.



Job Title: Python/JAVA/Django Developer

Location: East Hartford, CT

Duration: Long Term Contrac......" />
                    <meta itemprop="url" content="http://jobview.monster.com/python-java-django-developer-job-east-hartford-ct-us-182475182.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary has-bolding">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="10" data-m_impr_j_coc="xw267993766wx" data-m_impr_j_jawsid="218499340" data-m_impr_j_jobid="181233697" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="38.8858" data-m_impr_j_lid="895" data-m_impr_j_long="-77.0951" data-m_impr_j_occid="11993" data-m_impr_j_p="5" data-m_impr_j_postingid="8766d6b1-b351-4bd2-b6eb-0627f88dd676" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="78535510-6751-4112-982c-2c00065efd3e" href="http://jobview.monster.com/python-django-developers-wanted-job-arlington-va-us-181233697.aspx?mescoid=1500129001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;5&#39;});; clickJobTitle(&#39;plid=895&amp;pcid=10&amp;poccid=11993&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Python/Django Developers Wanted&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xw267993766wx_SuperStar.com&quot;,&quot;eVar31&quot;:&quot;arlington_VA_22201&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-02-28T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Python/Django Developers Wanted"><span itemprop="title">Python/Django Developers Wanted</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-superstar__2ecom.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;5&#39;});" rel="nofollow" title="SuperStar.com"><span itemprop="name">SuperStar.com</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-arlington,-va.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;5&#39;});" title="arlington, VA, 22201"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    arlington, VA
            <meta itemprop="addressLocality" content="arlington" />
            <meta itemprop="addressRegion" content="VA" />
            <meta itemprop="postalCode" content="22201" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-02-28T12:00" itemprop="datePosted">+30 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="SuperStar Inc, Established in 2003 is located in Arlington, VA and is metro AccessibleWe are looking for a talented Python developer(s) to join our dynamic team.We  offer competitive salaries with comprehensive benefits package  including medical, d......" />
                    <meta itemprop="url" content="http://jobview.monster.com/python-django-developers-wanted-job-arlington-va-us-181233697.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xsmartsynergiesx" data-m_impr_j_jawsid="230917748" data-m_impr_j_jobid="183173717" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="38.8951" data-m_impr_j_lid="371" data-m_impr_j_long="-77.0364" data-m_impr_j_occid="11970" data-m_impr_j_p="6" data-m_impr_j_postingid="5d230803-94bb-4d85-a1a1-e5950feb0c2e" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="2528b4dc-afe3-4226-92b9-7e1512ca2435" href="http://jobview.monster.com/python-django-developer-job-washington-dc-us-183173717.aspx?mescoid=1500129001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;6&#39;});; clickJobTitle(&#39;plid=371&amp;pcid=660&amp;poccid=11970&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Python/Django Developer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xsmartsynergiesx_Smart Synergies Inc&quot;,&quot;eVar31&quot;:&quot;Washington_DC_&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-19T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Python/Django Developer"><span itemprop="title">Python/Django Developer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-smart-synergies.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;6&#39;});" title="Smart Synergies Inc"><span itemprop="name">Smart Synergies Inc</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-washington,-dc.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;6&#39;});" title="Washington, DC"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Washington, DC
            <meta itemprop="addressLocality" content="Washington" />
            <meta itemprop="addressRegion" content="DC" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-19T12:00" itemprop="datePosted">1 day ago</time></p>
                    </div>
                    <meta itemprop="description" content="3-5 years of Python Django or Flask development experience.
As part of this role you will serve as Python/Django developer on a team at a Federal Government with an information-sharing mission. Be part of a dynamic team that works closely with the c......" />
                    <meta itemprop="url" content="http://jobview.monster.com/python-django-developer-job-washington-dc-us-183173717.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="4" data-m_impr_j_coc="xocr1340829_javx" data-m_impr_j_jawsid="207364219" data-m_impr_j_jobid="179114121" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="37.3872" data-m_impr_j_lid="883" data-m_impr_j_long="-122.0744" data-m_impr_j_occid="11900" data-m_impr_j_p="7" data-m_impr_j_postingid="e10244c7-83af-4ada-bfba-62a23ea2e603" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="c00d11ec-902f-4948-ab17-eacbc632f902" href="http://jobview.monster.com/seeking-a-python-javascript-full-stack-engineer-in-mountain-view-ca-job-mountain-view-ca-us-179114121.aspx?mescoid=1500127001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;7&#39;});; clickJobTitle(&#39;plid=883&amp;pcid=4&amp;poccid=11900&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Seeking a Python, JavaScript Full Stack Engineer in Mountain View, CA&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xocr1340829_javx_OSI Engineering&quot;,&quot;eVar31&quot;:&quot;Mountain View_CA_94041&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-14T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Seeking a Python, JavaScript Full Stack Engineer in Mountain View, CA"><span itemprop="title">Seeking a Python, JavaScript Full Stack Engineer in Mountain View, CA</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-osi-engineering.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;7&#39;});" rel="nofollow" title="OSI Engineering"><span itemprop="name">OSI Engineering</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-mountain-view,-ca.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;7&#39;});" title="Mountain View, CA, 94041"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Mountain View, CA
            <meta itemprop="addressLocality" content="Mountain View" />
            <meta itemprop="addressRegion" content="CA" />
            <meta itemprop="postalCode" content="94041" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-14T12:00" itemprop="datePosted">6 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Responsibilities
• Responsible for the development of web applications enabling hardware and software teams.
• Develop data analytic solutions for regression tracking.
• Design and implement a MySQL DB to store and to generate regression data.
• Wo......" />
                    <meta itemprop="url" content="http://jobview.monster.com/seeking-a-python-javascript-full-stack-engineer-in-mountain-view-ca-job-mountain-view-ca-us-179114121.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xevgrquadx" data-m_impr_j_jawsid="229408496" data-m_impr_j_jobid="182907351" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="0" data-m_impr_j_lid="696" data-m_impr_j_long="0" data-m_impr_j_occid="11904" data-m_impr_j_p="8" data-m_impr_j_postingid="914f003f-a47c-45f0-b501-9de5586fa001" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="e68533c9-c5fb-4483-89c1-2a232a6d2857" href="http://jobview.monster.com/developer-python-django-job-washington-dc-dc-us-182907351.aspx?mescoid=1500127001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;8&#39;});; clickJobTitle(&#39;plid=696&amp;pcid=660&amp;poccid=11904&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Developer - Python/Django&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xevgrquadx_Quadrant Inc&quot;,&quot;eVar31&quot;:&quot;Washington DC_DC_&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-11T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Developer - Python/Django"><span itemprop="title">Developer - Python/Django</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-quadrant-inc.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;8&#39;});" rel="nofollow" title="Quadrant Inc"><span itemprop="name">Quadrant Inc</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-district-of-columbia.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;8&#39;});" title="Washington DC, DC"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Washington DC, DC
            <meta itemprop="addressLocality" content="Washington DC" />
            <meta itemprop="addressRegion" content="DC" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-11T12:00" itemprop="datePosted">9 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Sr. Python Django Developer
              Washington, D.C

              MUST:
      Experienced Python Django developer
10 years of overall (OOP) programming experience
5-7 years of solid Pyth......" />
                    <meta itemprop="url" content="http://jobview.monster.com/developer-python-django-job-washington-dc-dc-us-182907351.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="" data-m_impr_j_jawsid="165528239" data-m_impr_j_jobid="0" data-m_impr_j_jpm="1" data-m_impr_j_jpt="2" data-m_impr_j_lat="38.9695" data-m_impr_j_lid="693" data-m_impr_j_long="-77.3861" data-m_impr_j_occid="11969" data-m_impr_j_p="9" data-m_impr_j_postingid="b9199795-dcba-49d2-abf3-9cba2f412481" data-m_impr_j_pvc="e8df50dd-c265-4c46-a96b-efc234d6a44e" data-m_impr_s_t="t" data-m_impr_uuid="f5b3586e-68dc-41c9-bcb5-ab6adfe2a2b4" href="http://job-openings.monster.com/monster/b9199795-dcba-49d2-abf3-9cba2f412481?mescoid=1500127001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;9&#39;});; clickJobTitle(&#39;plid=693&amp;pcid=660&amp;poccid=11969&#39;,&#39;Python&#39;,&#39;&#39;)" rel="nofollow" target="_blank" title="Cyber Developer - Linux Development (C / C++ / Python)"><span itemprop="title">Cyber Developer - Linux Development (C / C++ / Python)</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-lockheed-martin.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;9&#39;});" title="Lockheed Martin"><span itemprop="name">Lockheed Martin</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-herndon,-va.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;9&#39;});" title="Herndon, VA"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Herndon, VA
            <meta itemprop="addressLocality" content="Herndon" />
            <meta itemprop="addressRegion" content="VA" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2016-07-21T12:00" itemprop="datePosted">+30 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Req ID :
355681BR

Job Code/Title :
E2564:Cyber Architect Stf

Job Description :
Do you have a passion for low-level code development? Do you pride yourself on solving problems that others think are impossible? If you answered yes to these questions......" />
                    <meta itemprop="url" content="http://job-openings.monster.com/monster/b9199795-dcba-49d2-abf3-9cba2f412481" />
                    <meta itemprop="employmentType" content="" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xkforcex" data-m_impr_j_jawsid="228470100" data-m_impr_j_jobid="182696971" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="40.7564" data-m_impr_j_lid="550" data-m_impr_j_long="-73.9827" data-m_impr_j_occid="11969" data-m_impr_j_p="10" data-m_impr_j_postingid="7d133d77-82ae-4352-b248-1c3df2a417cd" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="04a624b1-74ef-4ae3-8df1-1d3fc58bdf92" href="http://jobview.monster.com/python-developer-job-new-york-ny-us-182696971.aspx?mescoid=1500127001001&amp;jobPosition=2" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;10&#39;});; clickJobTitle(&#39;plid=550&amp;pcid=660&amp;poccid=11969&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Python Developer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xkforcex_Kforce Inc&quot;,&quot;eVar31&quot;:&quot;New York_NY_10175&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-20T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Python Developer"><span itemprop="title">Python Developer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-kforce-professional-staffing.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;10&#39;});" title="Kforce Inc"><span itemprop="name">Kforce Inc</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-new-york-city,-ny.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;10&#39;});" title="New York, NY, 10175"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    New York, NY
            <meta itemprop="addressLocality" content="New York" />
            <meta itemprop="addressRegion" content="NY" />
            <meta itemprop="postalCode" content="10175" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-20T12:00" itemprop="datePosted">Posted today</time></p>
                    </div>
                    <meta itemprop="description" content="RESPONSIBILITIES:Kforce has a client seeking a Python Developer in New York, New York (NY).    Overview: This is a well-known company that consumes online data, TV, and radio from around the world to provide real time search results and media viewin......" />
                    <meta itemprop="url" content="http://jobview.monster.com/python-developer-job-new-york-ny-us-182696971.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="x549889HJSx" data-m_impr_j_jawsid="229965682" data-m_impr_j_jobid="182997939" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="41.8128" data-m_impr_j_lid="368" data-m_impr_j_long="-72.6976" data-m_impr_j_occid="11904" data-m_impr_j_p="11" data-m_impr_j_postingid="6633582a-97a7-491b-ab25-1ae7234c2c16" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="bb755c07-b485-4e74-a709-3156b507bac2" href="http://jobview.monster.com/python-developer-job-blue-hills-ct-us-182997939.aspx?mescoid=1500127001001&amp;jobPosition=2" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;11&#39;});; clickJobTitle(&#39;plid=368&amp;pcid=660&amp;poccid=11904&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Python Developer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;x549889HJSx_Tekmark Global Solutions&quot;,&quot;eVar31&quot;:&quot;Blue Hills_CT_&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-13T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Python Developer"><span itemprop="title">Python Developer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-tekmark-global-solutions.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;11&#39;});" rel="nofollow" title="Tekmark Global Solutions"><span itemprop="name">Tekmark Global Solutions</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-connecticut.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;11&#39;});" title="Blue Hills, CT"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Blue Hills, CT
            <meta itemprop="addressLocality" content="Blue Hills" />
            <meta itemprop="addressRegion" content="CT" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-13T12:00" itemprop="datePosted">7 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Job Description:

-Client is seeking a Python Developer.



Qualifications:

-3+ years of experience with core Python development

-3+ years of experience with Oracle / DB2 databases

-SAS experience is a plus

-Experience with the following tool......" />
                    <meta itemprop="url" content="http://jobview.monster.com/python-developer-job-blue-hills-ct-us-182997939.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
                    <div class="js_result_container featured-ad clearfix">
                        <script language="javaScript" type="text/javascript" id="AdScript_Left1_FeaturedJob" name="AdScript_Left1_FeaturedJob">
	var OAS_RNS = 028637960;
                                                        var OAS_taxonomy='site=mons&affiliate=mons&app=js&size=0x101&oas_pv=no_analytics&key=python&fb=0&cy=US&sapp=jsr&app=js';
                                                        var OAS_query='site=mons&affiliate=mons&app=js&size=0x101&oas_pv=no_analytics&key=python&fb=0&cy=US&sapp=jsr&app=js';
	                                                    OAS_query == '' ? OAS_query+='XE' + '&' + OAS_taxonomy + OAS_rdl + "&if_nt_CookieAccept=" + OAS_CA + '&XE': OAS_query+= '&XE' + '&' + OAS_taxonomy + OAS_rdl + "&if_nt_CookieAccept=" + OAS_CA + '&XE';
	                                                    document.write('<iframe width=100% height=101 id=AdFrame_Left1_FeaturedJob name=AdFrame_Left1_FeaturedJob class="" marginwidth=0 marginheight=0 hspace=0 vspace=0 frameborder=0 scrolling=no bordercolor="#000000" src="https://oas.monster.com/RealMedia/ads/adstream_sx.ads/us.monster.en/jsrnew/powersearch.aspx/1' + OAS_RNS + '@Middle,BottomRight,Left1,Left2,Middle1,Left3,Right3,Right,Right1,Right2,x42,x18,Bottom1,Top,TopRight!Left1?' + OAS_query + '" title="Advertisement"></iframe>');

</script>
                    </div>
                    <div class="js_result_container featured-ad clearfix">
                        <script language="javaScript" type="text/javascript" id="AdScript_Left2_FeaturedOpportunity" name="AdScript_Left2_FeaturedOpportunity">
	var OAS_RNS = 028637960;
                                                        var OAS_taxonomy='site=mons&affiliate=mons&app=js&size=0x101&oas_pv=no_analytics&key=python&fb=0&cy=US&sapp=jsr&app=js';
                                                        var OAS_query='site=mons&affiliate=mons&app=js&size=0x101&oas_pv=no_analytics&key=python&fb=0&cy=US&sapp=jsr&app=js';
	                                                    OAS_query == '' ? OAS_query+='XE' + '&' + OAS_taxonomy + OAS_rdl + "&if_nt_CookieAccept=" + OAS_CA + '&XE': OAS_query+= '&XE' + '&' + OAS_taxonomy + OAS_rdl + "&if_nt_CookieAccept=" + OAS_CA + '&XE';
	                                                    document.write('<iframe width=100% height=101 id=AdFrame_Left2_FeaturedOpportunity name=AdFrame_Left2_FeaturedOpportunity class="" marginwidth=0 marginheight=0 hspace=0 vspace=0 frameborder=0 scrolling=no bordercolor="#000000" src="https://oas.monster.com/RealMedia/ads/adstream_sx.ads/us.monster.en/jsrnew/powersearch.aspx/1' + OAS_RNS + '@Middle,BottomRight,Left1,Left2,Middle1,Left3,Right3,Right,Right1,Right2,x42,x18,Bottom1,Top,TopRight!Left2?' + OAS_query + '" title="Advertisement"></iframe>');

</script>
                    </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xmotivwax" data-m_impr_j_jawsid="229937225" data-m_impr_j_jobid="182989858" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="47.6157" data-m_impr_j_lid="647" data-m_impr_j_long="-122.3445" data-m_impr_j_occid="11970" data-m_impr_j_p="12" data-m_impr_j_postingid="01a168d4-4361-4261-a813-59093c4dd248" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="7f64c0d1-f93c-47bb-b17a-84513e6d7cf1" href="http://jobview.monster.com/senior-python-developer-job-seattle-wa-us-182989858.aspx?mescoid=1500127001001&amp;jobPosition=2" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;12&#39;});; clickJobTitle(&#39;plid=647&amp;pcid=660&amp;poccid=11970&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Senior Python Developer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xmotivwax_Motiv, Inc.&quot;,&quot;eVar31&quot;:&quot;Seattle_WA_98121&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-13T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Senior Python Developer"><span itemprop="title">Senior Python Developer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-motiv__2c-inc__2e.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;12&#39;});" rel="nofollow" title="Motiv, Inc."><span itemprop="name">Motiv, Inc.</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-seattle,-wa.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;12&#39;});" title="Seattle, WA, 98121"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Seattle, WA
            <meta itemprop="addressLocality" content="Seattle" />
            <meta itemprop="addressRegion" content="WA" />
            <meta itemprop="postalCode" content="98121" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-13T12:00" itemprop="datePosted">7 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="We are looking for an outstanding Senior Software Developer to join our team and assist our client in the Greater Seattle Area.  This team is responsible for creating an innovative new system from the ground up! The company has amazing work life bal......" />
                    <meta itemprop="url" content="http://jobview.monster.com/senior-python-developer-job-seattle-wa-us-182989858.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xw105012055wx" data-m_impr_j_jawsid="221929603" data-m_impr_j_jobid="181672808" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="40.3679" data-m_impr_j_lid="532" data-m_impr_j_long="-74.6543" data-m_impr_j_occid="12005" data-m_impr_j_p="13" data-m_impr_j_postingid="8eb3659e-d780-4877-ad1d-58d3d7a02f1f" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="cd99b77e-95ec-4ba5-896e-df2b05c1bf2e" href="http://jobview.monster.com/cloud-python-developer-job-princeton-township-nj-us-181672808.aspx?mescoid=1500127001001&amp;jobPosition=2" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;13&#39;});; clickJobTitle(&#39;plid=532&amp;pcid=660&amp;poccid=12005&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Cloud/Python Developer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xw105012055wx_Systech International&quot;,&quot;eVar31&quot;:&quot;Princeton Township_NJ_08540&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-12T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Cloud/Python Developer"><span itemprop="title">Cloud/Python Developer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-systech-international.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;13&#39;});" rel="nofollow" title="Systech International"><span itemprop="name">Systech International</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-new-jersey.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;13&#39;});" title="Princeton Township, NJ, 08540"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Princeton Township, NJ
            <meta itemprop="addressLocality" content="Princeton Township" />
            <meta itemprop="addressRegion" content="NJ" />
            <meta itemprop="postalCode" content="08540" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-12T12:00" itemprop="datePosted">8 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Highly skilled individual with proven track record building cloud solutions: Has effective development style and can drive a sense of urgency.  Successful candidate will extend and maintain existing functionality of cloud offering, and be fully invo......" />
                    <meta itemprop="url" content="http://jobview.monster.com/cloud-python-developer-job-princeton-township-nj-us-181672808.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xbartx" data-m_impr_j_jawsid="229635598" data-m_impr_j_jobid="182931848" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="37.3393" data-m_impr_j_lid="356" data-m_impr_j_long="-121.895" data-m_impr_j_occid="11904" data-m_impr_j_p="14" data-m_impr_j_postingid="080f4ce7-84c6-4f40-89a5-2870c0875b42" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="eeb9c380-0c8b-4708-8d0c-1a1398083ed2" href="http://jobview.monster.com/python-developer-job-san-jose-ca-us-182931848.aspx?mescoid=1500127001001&amp;jobPosition=2" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;14&#39;});; clickJobTitle(&#39;plid=356&amp;pcid=660&amp;poccid=11904&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Python Developer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xbartx_The Bartech Group&quot;,&quot;eVar31&quot;:&quot;San Jose_CA_&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-12T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Python Developer"><span itemprop="title">Python Developer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-the-bartech-group.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;14&#39;});" title="The Bartech Group"><span itemprop="name">The Bartech Group</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-san-jose,-ca.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;14&#39;});" title="San Jose, CA"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    San Jose, CA
            <meta itemprop="addressLocality" content="San Jose" />
            <meta itemprop="addressRegion" content="CA" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-12T12:00" itemprop="datePosted">8 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Job Description
  Location: San Jose, CA 95131
 Pay Rate: $85.00 per hour

  If you are an experienced Python Developer looking for a position with a leading company, Bartech can help! We are a leading staffing firm and our clients include some of......" />
                    <meta itemprop="url" content="http://jobview.monster.com/python-developer-job-san-jose-ca-us-182931848.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xnbs1x" data-m_impr_j_jawsid="226060699" data-m_impr_j_jobid="182287507" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="35.7589" data-m_impr_j_lid="511" data-m_impr_j_long="-78.7808" data-m_impr_j_occid="11970" data-m_impr_j_p="15" data-m_impr_j_postingid="ae88be79-049d-4cce-abc1-a5b76a26fe56" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="78769a6a-2d35-4e8e-ac42-1bf5deafc64a" href="http://jobview.monster.com/full-stack-python-engineer-job-cary-nc-us-182287507.aspx?mescoid=1500127001001&amp;jobPosition=2" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;15&#39;});; clickJobTitle(&#39;plid=511&amp;pcid=660&amp;poccid=11970&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Full Stack Python Engineer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xnbs1x_Randstad Technologies&quot;,&quot;eVar31&quot;:&quot;Cary_NC_27511&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-10T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Full Stack Python Engineer"><span itemprop="title">Full Stack Python Engineer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-randstad-technologies.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;15&#39;});" rel="nofollow" title="Randstad Technologies"><span itemprop="name">Randstad Technologies</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-cary,-nc.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;15&#39;});" title="Cary, NC, 27511"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Cary, NC
            <meta itemprop="addressLocality" content="Cary" />
            <meta itemprop="addressRegion" content="NC" />
            <meta itemprop="postalCode" content="27511" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-10T12:00" itemprop="datePosted">10 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Python Full Stack Engineer


DIRECT HIRE/PERM


Please forward your resume directly to debra.reed@randstadusa.com.  As a qualified applicant we will respond back to you same business day.  Once we discuss the position and your qualifications, a p......" />
                    <meta itemprop="url" content="http://jobview.monster.com/full-stack-python-engineer-job-cary-nc-us-182287507.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xaditicinx" data-m_impr_j_jawsid="228044969" data-m_impr_j_jobid="182601362" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="47.5766" data-m_impr_j_lid="647" data-m_impr_j_long="-122.3316" data-m_impr_j_occid="11970" data-m_impr_j_p="16" data-m_impr_j_postingid="6c4e4a7a-602a-478b-82f2-f676de56bfd3" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="2052d5ef-92e5-41c4-9caf-b51b491de87f" href="http://jobview.monster.com/python-developer-job-seattle-wa-us-182601362.aspx?mescoid=1500127001001&amp;jobPosition=2" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;16&#39;});; clickJobTitle(&#39;plid=647&amp;pcid=660&amp;poccid=11970&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Python developer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xaditicinx_Aditi Staffing Private Limited&quot;,&quot;eVar31&quot;:&quot;Seattle_WA_98134&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-04T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Python developer"><span itemprop="title">Python developer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-aditi-staffing-private-limited.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;16&#39;});" rel="nofollow" title="Aditi Staffing Private Limited"><span itemprop="name">Aditi Staffing Private Limited</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-seattle,-wa.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;16&#39;});" title="Seattle, WA, 98134"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Seattle, WA
            <meta itemprop="addressLocality" content="Seattle" />
            <meta itemprop="addressRegion" content="WA" />
            <meta itemprop="postalCode" content="98134" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-04T12:00" itemprop="datePosted">16 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="PYTHON FULL STACK DEVELOPER **



Evaluating analytics to make data driven recommendations for web design and to measure success of incremental innovation. Producing Interaction Design Documents and Functional Specifications through annotated wire......" />
                    <meta itemprop="url" content="http://jobview.monster.com/python-developer-job-seattle-wa-us-182601362.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xsoftcomnjx" data-m_impr_j_jawsid="217321327" data-m_impr_j_jobid="181055025" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="40.7583" data-m_impr_j_lid="549" data-m_impr_j_long="-73.7194" data-m_impr_j_occid="11970" data-m_impr_j_p="17" data-m_impr_j_postingid="fe6484bf-ddd8-4462-bdc7-4b3958fa9f69" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="6b88b276-16a0-41a7-9cb9-44f89d71d648" href="http://jobview.monster.com/sr-python-developer-job-floral-park-ny-us-181055025.aspx?mescoid=1500127001001&amp;jobPosition=2" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;17&#39;});; clickJobTitle(&#39;plid=549&amp;pcid=660&amp;poccid=11970&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Sr. Python Developer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xsoftcomnjx_Softcom Systems Inc.&quot;,&quot;eVar31&quot;:&quot;Floral Park_NY_11005&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-03-22T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Sr. Python Developer"><span itemprop="title">Sr. Python Developer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-softcom-systems-inc__2e.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;17&#39;});" rel="nofollow" title="Softcom Systems Inc."><span itemprop="name">Softcom Systems Inc.</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-floral-park,-ny.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;17&#39;});" title="Floral Park, NY, 11005"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Floral Park, NY
            <meta itemprop="addressLocality" content="Floral Park" />
            <meta itemprop="addressRegion" content="NY" />
            <meta itemprop="postalCode" content="11005" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-03-22T12:00" itemprop="datePosted">29 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="One of my clients is looking for a Sr.Sr. Python Developer for a Direct hire position.  If you are qualified and perfect match for the below mentioned position, forward your resumes to kiran@softcomsystems.com  Along with 2 professional references(F......" />
                    <meta itemprop="url" content="http://jobview.monster.com/sr-python-developer-job-floral-park-ny-us-181055025.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xfaberginx" data-m_impr_j_jawsid="224464996" data-m_impr_j_jobid="182072378" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="41.8858" data-m_impr_j_lid="417" data-m_impr_j_long="-87.6229" data-m_impr_j_occid="11970" data-m_impr_j_p="18" data-m_impr_j_postingid="3b45b6c8-36cd-49f5-a35a-f59ed79e20cc" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="5429d9e7-37d5-446f-b6f7-db08ba61da47" href="http://jobview.monster.com/python-developer-6-12-months-contract-job-chicago-il-us-182072378.aspx?mescoid=1500127001001&amp;jobPosition=2" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;18&#39;});; clickJobTitle(&#39;plid=417&amp;pcid=660&amp;poccid=11970&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Python Developer - 6-12 Months Contract&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xfaberginx_Fabergent&quot;,&quot;eVar31&quot;:&quot;Chicago_IL_60601&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-18T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Python Developer - 6-12 Months Contract"><span itemprop="title">Python Developer - 6-12 Months Contract</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-fabergent.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;18&#39;});" title="Fabergent"><span itemprop="name">Fabergent</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-chicago,-il.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;18&#39;});" title="Chicago, IL, 60601"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Chicago, IL
            <meta itemprop="addressLocality" content="Chicago" />
            <meta itemprop="addressRegion" content="IL" />
            <meta itemprop="postalCode" content="60601" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-18T12:00" itemprop="datePosted">2 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="SUMMARY:


- &#183;         Looking for a 3-5 years of Python Development.
- &#183;         In this position you will be working in a DevOps environment and initially responsible for maintenance and bug fixes for our client’s in-house ATS software.
- &#183;    ......" />
                    <meta itemprop="url" content="http://jobview.monster.com/python-developer-6-12-months-contract-job-chicago-il-us-182072378.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xetouchsysx" data-m_impr_j_jawsid="227234062" data-m_impr_j_jobid="182493103" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="37.7749" data-m_impr_j_lid="355" data-m_impr_j_long="-122.4195" data-m_impr_j_occid="11904" data-m_impr_j_p="19" data-m_impr_j_postingid="899fc66e-2f71-45b1-a1a1-d11e702879ec" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="e82e97f6-01ef-41d5-b1eb-f96f146ed360" href="http://jobview.monster.com/python-engineer-job-san-francisco-ca-us-182493103.aspx?mescoid=1500127001001&amp;jobPosition=2" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;19&#39;});; clickJobTitle(&#39;plid=355&amp;pcid=660&amp;poccid=11904&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Python Engineer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xetouchsysx_etouch Systems Corp&quot;,&quot;eVar31&quot;:&quot;San Francisco_CA_&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-03-31T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Python Engineer"><span itemprop="title">Python Engineer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-etouch-systems-corp.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;19&#39;});" title="etouch Systems Corp"><span itemprop="name">etouch Systems Corp</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-san-francisco,-ca.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;19&#39;});" title="San Francisco, CA"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    San Francisco, CA
            <meta itemprop="addressLocality" content="San Francisco" />
            <meta itemprop="addressRegion" content="CA" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-03-31T12:00" itemprop="datePosted">20 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Python Engineer

12 months+

San Francisco CAResponsibilities:
- Take ownership over project timelines and deliverables
- Contribute to the design, architecture and build of our Core Platform
- Help scale the platform and build out new features
- Co......" />
                    <meta itemprop="url" content="http://jobview.monster.com/python-engineer-job-san-francisco-ca-us-182493103.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xavestax" data-m_impr_j_jawsid="226691670" data-m_impr_j_jobid="182394144" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="37.3435" data-m_impr_j_lid="356" data-m_impr_j_long="-121.8887" data-m_impr_j_occid="11904" data-m_impr_j_p="20" data-m_impr_j_postingid="9063a1d6-869b-463e-9ab7-b3afc00bb06a" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="77a0f1f6-cd74-4bec-ae18-923ff757d957" href="http://jobview.monster.com/python-engineer-consultant-ii-job-san-jose-ca-us-182394144.aspx?mescoid=1500127001001&amp;jobPosition=2" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;20&#39;});; clickJobTitle(&#39;plid=356&amp;pcid=660&amp;poccid=11904&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Python Engineer-Consultant II&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xavestax_Avesta Computer Services&quot;,&quot;eVar31&quot;:&quot;San Jose_CA_95101&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-03-29T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Python Engineer-Consultant II"><span itemprop="title">Python Engineer-Consultant II</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-avesta-computer-services.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;20&#39;});" rel="nofollow" title="Avesta Computer Services"><span itemprop="name">Avesta Computer Services</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-san-jose,-ca.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;20&#39;});" title="San Jose, CA, 95101"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    San Jose, CA
            <meta itemprop="addressLocality" content="San Jose" />
            <meta itemprop="addressRegion" content="CA" />
            <meta itemprop="postalCode" content="95101" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-03-29T12:00" itemprop="datePosted">22 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Our Client is the largest networking company in the world.They develops, manufactures, and sells networking hardware,telecommunications equipment and other high technology services and products.They are specializes into specific tech markets, such a......" />
                    <meta itemprop="url" content="http://jobview.monster.com/python-engineer-consultant-ii-job-san-jose-ca-us-182394144.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xtechminx" data-m_impr_j_jawsid="230935871" data-m_impr_j_jobid="183183020" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="37.386" data-m_impr_j_lid="883" data-m_impr_j_long="-122.0839" data-m_impr_j_occid="11970" data-m_impr_j_p="21" data-m_impr_j_postingid="3013d79a-5ad3-4336-8879-bea918f40520" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="484e1b2c-6101-4dd4-bbb9-5d7919d209a0" href="http://jobview.monster.com/python-developer-job-mountain-view-ca-us-183183020.aspx?mescoid=1500127001001&amp;jobPosition=2" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;21&#39;});; clickJobTitle(&#39;plid=883&amp;pcid=660&amp;poccid=11970&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Python Developer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xtechminx_Tech Mahindra Limited&quot;,&quot;eVar31&quot;:&quot;Mountain View_CA_&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-19T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Python Developer"><span itemprop="title">Python Developer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-tech-mahindra-limited.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;21&#39;});" rel="nofollow" title="Tech Mahindra Limited"><span itemprop="name">Tech Mahindra Limited</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-mountain-view,-ca.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;21&#39;});" title="Mountain View, CA"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Mountain View, CA
            <meta itemprop="addressLocality" content="Mountain View" />
            <meta itemprop="addressRegion" content="CA" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-19T12:00" itemprop="datePosted">1 day ago</time></p>
                    </div>
                    <meta itemprop="description" content="Python Developer with Mobile / Automation Experience opportunity situated in Mountain View, CA and the length is Full-time / Contract on w2.  Required:•    Proficiency in Python, C++, or Java•    Linux Development Environment•    Experience setting ......" />
                    <meta itemprop="url" content="http://jobview.monster.com/python-developer-job-mountain-view-ca-us-183183020.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xprimesystechnolx" data-m_impr_j_jawsid="175753321" data-m_impr_j_jobid="171837225" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="40.5745" data-m_impr_j_lid="550" data-m_impr_j_long="-74.4149" data-m_impr_j_occid="11882" data-m_impr_j_p="22" data-m_impr_j_postingid="fee7c377-d7f5-4aff-ae90-89953da9351f" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="2103be21-19c6-44ae-9bec-917b6fc6e13a" href="http://jobview.monster.com/jr-python-or-scala-developer-job-south-plainfield-nj-us-171837225.aspx?mescoid=1500127001001&amp;jobPosition=2" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;22&#39;});; clickJobTitle(&#39;plid=550&amp;pcid=660&amp;poccid=11882&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Jr Python or Scala Developer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xprimesystechnolx_PRIMESYS TECHNOLOGIES&quot;,&quot;eVar31&quot;:&quot;South Plainfield_NJ_07080&quot;,&quot;prop22&quot;:&quot;Per Diem&quot;,&quot;prop24&quot;:&quot;2017-04-11T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Jr Python or Scala Developer"><span itemprop="title">Jr Python or Scala Developer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-primesys-technologies.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;22&#39;});" rel="nofollow" title="PRIMESYS TECHNOLOGIES"><span itemprop="name">PRIMESYS TECHNOLOGIES</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-south-plainfield,-nj.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;22&#39;});" title="South Plainfield, NJ, 07080"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    South Plainfield, NJ
            <meta itemprop="addressLocality" content="South Plainfield" />
            <meta itemprop="addressRegion" content="NJ" />
            <meta itemprop="postalCode" content="07080" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-11T12:00" itemprop="datePosted">9 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="We are looking for Junior Python or Scala Developers for a long term contract role for our clients. Please note these jobs are for consulting roles only.





Local to New Jersey area are preferred
1 to 2 Years of experience profiles will be given ......" />
                    <meta itemprop="url" content="http://jobview.monster.com/jr-python-or-scala-developer-job-south-plainfield-nj-us-171837225.aspx" />
                    <meta itemprop="employmentType" content="Per Diem" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="x551813hjsx" data-m_impr_j_jawsid="229135893" data-m_impr_j_jobid="182825475" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="40.7142" data-m_impr_j_lid="550" data-m_impr_j_long="-74.006" data-m_impr_j_occid="11904" data-m_impr_j_p="23" data-m_impr_j_postingid="4b41cda6-43e0-498b-add7-fe2a2b10d240" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="12f51e53-57fe-4b71-bb79-d1634d199684" href="http://jobview.monster.com/python-developer-job-new-york-city-ny-us-182825475.aspx?mescoid=1500127001001&amp;jobPosition=2" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;23&#39;});; clickJobTitle(&#39;plid=550&amp;pcid=660&amp;poccid=11904&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;PYTHON DEVELOPER&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;x551813hjsx_Staffing Solutions USA, Inc.&quot;,&quot;eVar31&quot;:&quot;New York City_NY_&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-10T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="PYTHON DEVELOPER"><span itemprop="title">PYTHON DEVELOPER</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-staffing-solutions-usa__2c-inc__2e.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;23&#39;});" rel="nofollow" title="Staffing Solutions USA, Inc."><span itemprop="name">Staffing Solutions USA, Inc.</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-new-york-city,-ny.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;23&#39;});" title="New York City, NY"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    New York City, NY
            <meta itemprop="addressLocality" content="New York City" />
            <meta itemprop="addressRegion" content="NY" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-10T12:00" itemprop="datePosted">10 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="PYTHON DEVELOPER

Our financial client is looking for a person with strong development experience in Python that comes from the financial services industry and has worked in a Linux/ Unix environment.

Responsibilities:



Strong development experi......" />
                    <meta itemprop="url" content="http://jobview.monster.com/python-developer-job-new-york-city-ny-us-182825475.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xw247985740wx" data-m_impr_j_jawsid="228938848" data-m_impr_j_jobid="182773102" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="45.4461" data-m_impr_j_lid="578" data-m_impr_j_long="-122.9838" data-m_impr_j_occid="11904" data-m_impr_j_p="24" data-m_impr_j_postingid="65fcca77-0c04-418a-9702-1643f73b77f1" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="50de2935-0835-4aed-9e20-a07f609e66db" href="http://jobview.monster.com/python-developer-job-hillsboro-or-us-182773102.aspx?mescoid=1500127001001&amp;jobPosition=2" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;24&#39;});; clickJobTitle(&#39;plid=578&amp;pcid=660&amp;poccid=11904&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Python Developer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xw247985740wx_Macropace Technologies&quot;,&quot;eVar31&quot;:&quot;Hillsboro_OR_97123&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-08T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Python Developer"><span itemprop="title">Python Developer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-macropace-technologies.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;24&#39;});" rel="nofollow" title="Macropace Technologies"><span itemprop="name">Macropace Technologies</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-hillsboro,-or.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;24&#39;});" title="Hillsboro, OR, 97123"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Hillsboro, OR
            <meta itemprop="addressLocality" content="Hillsboro" />
            <meta itemprop="addressRegion" content="OR" />
            <meta itemprop="postalCode" content="97123" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-08T12:00" itemprop="datePosted">12 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Python Developer

Hillsboro, OR

Full Time Position



Job Description:

Experience in developing Test Automation frameworks using Python/ C#/C ++

Familiar with any one Scripting language – Python/Perl

Strong debugging skills, someone who has exp......" />
                    <meta itemprop="url" content="http://jobview.monster.com/python-developer-job-hillsboro-or-us-182773102.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xcomsysfoxx" data-m_impr_j_jawsid="228754979" data-m_impr_j_jobid="182746774" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="47.6062" data-m_impr_j_lid="647" data-m_impr_j_long="-122.3321" data-m_impr_j_occid="11904" data-m_impr_j_p="25" data-m_impr_j_postingid="6c2f02c5-73d1-4682-9a35-659e7ed31505" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="2932621d-bc30-4864-aab2-912337984a07" href="http://jobview.monster.com/sdet-java-python-job-seattle-wa-us-182746774.aspx?mescoid=1500137001001&amp;jobPosition=2" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;25&#39;});; clickJobTitle(&#39;plid=647&amp;pcid=660&amp;poccid=11904&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;SDET (Java / Python)&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xcomsysfoxx_Experis&quot;,&quot;eVar31&quot;:&quot;Seattle_WA_&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-07T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="SDET (Java / Python)"><span itemprop="title">SDET (Java / Python)</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-experis.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;25&#39;});" rel="nofollow" title="Experis"><span itemprop="name">Experis</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-seattle,-wa.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;25&#39;});" title="Seattle, WA"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Seattle, WA
            <meta itemprop="addressLocality" content="Seattle" />
            <meta itemprop="addressRegion" content="WA" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-07T12:00" itemprop="datePosted">13 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Our client works at the intersection of Big Data and the Internet of Things to identify, locate and authenticate billions of items. Their Item Intelligence platform comprises the most comprehensive and widely adopted RAIN RFID product portfolio in t......" />
                    <meta itemprop="url" content="http://jobview.monster.com/sdet-java-python-job-seattle-wa-us-182746774.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
    </section>
<link rel="stylesheet" type="text/css" href="https://cdn.materialdesignicons.com/1.5.54/css/materialdesignicons.min.css" media="all">

        <div  id="twoColumnEmailWidget">

<input type="hidden" id="searchQuery" value="q=Python&amp;brd=1&amp;brd=2&amp;cy=US&amp;pp=25&amp;sort=rv.di.dt&amp;stp=TwoBoxBand" />
<input type="hidden" id="isLoggedIn" value="false" />
<input type="hidden" id="maxSaveSearchesAllowed" value="5" />
<input type="hidden" id="emailUrl" value="https://www.monster.com/jobs/emailjobs?q=Python" />
<input type="hidden" id="isDynamicPage" value="True"/>

        <div class="widget popup-widget reveal">
            <i id="widget-popup-close-icon" class="fa fa-close close-icon"></i>
            <div class="widget-head">
                <div class="marked-title clearfix">
                    <i class="fa fa-envelope"></i>
                    <h3>Get Python jobs by e-mail</h3>
                </div>
            </div>
            <div class="widget-content savedSearches">
                <div class="messageholder">

                </div>
                <div class="widget-content-inner">
                    <span class="save_search_header">We&#39;ll keep looking and send you new jobs that match this search. It&#39;s that simple!</span>
                    <label for="emailAddress" class="sr-only">Enter Your Email Address</label>
                    <div>
                        <input type="text" value="" id="emailAddress2" name="emailAddress2" placeholder="Enter Your Email Address" class="form-control">
                        <button data-loading-text="<i class='fa fa-spinner fa-spin'></i>" type="button" title="Email me Jobs" value="Email Me Jobs" onclick="dataLayer.push({'eventCategory':'Sidebar Widgets','eventAction':'JSA','eventLabel':'Click Link in Widget'});; emailActionTabClick(this); " id="emailButton2">
                            Email me Jobs
                        </button>
                        <span id="privacyMSG" class="litRegPrivacy">
                            By continuing you agree to Monster's <a title="privacy policy" target="_blank" href="http://my.monster.com/Privacy/Default.aspx">Privacy Policy</a>, <a title="terms of use" target="_blank" href="http://my.monster.com/Terms/Default.aspx">Terms of Use</a> and <a title="use of cookies" target="_blank" href="http://inside.monster.com/cookie-info/inside2.aspx">Use of Cookies</a>.
                        </span>

                    </div>
                </div>
            </div>
        </div>



        </div>


    <input type="hidden" id="totalPages" value="40" />
    <input type="hidden" id="prevText" value="Previous" />
    <input type="hidden" id="nextText" value="Next" />
    <input type="hidden" id="currentPage" value="1" />
    <div class="pagingWrapper">
        <div class="paging">

        </div>
    </div>
    <script type="text/javascript">
        $(function() {
            InitializePagingResultSet();
        });
    </script>

                </div>































<script src="https://logs.jobs.com/impression_trackingv2.js" type="text/javascript"></script>
            </div>
        </div>
    </div>

                <div id="topPopupEmailCardViewWidget">
                        <div id="jsa-top" class="widget popup-widget ">
        <i class="fa fa-close close-icon popup-close-icon"></i>
        <div class="widget-head">
            <div class="marked-title clearfix">
                <i class="fa fa-envelope"></i>
                <h3>Get Python jobs by e-mail</h3>
            </div>
        </div>
        <div class="widget-content savedSearches">
            <div class="error-box">
                <i class="fa fa-close close-icon error-box-close-icon"></i>
                <span class="error-msg"></span>
            </div>
            <span class="save_search_header success-msg"><strong>Success!</strong><br>Your search agent has been saved</span>
            <div class="widget-content-inner">
                <label for="emailAddress" class="sr-only">Enter Your Email Address</label>
                <div>
                        <input type="text" value="" name="emailAddressModalPopup" id="emailAddress" placeholder="Enter Your Email Address" class="emailAddressModalPopup form-control"/>
                    <button data-loading-text="<i class='fa fa-spinner fa-spin'></i>" type="button" title="Email Me Jobs " value="Email Me Jobs " class="emailButtonModalPopup">
                        Email Me Jobs
                    </button>
                            <div id="privacyMSG" class="litRegPrivacy">
                                By continuing you agree to Monster's <a title="privacy policy" target="_blank" href="http://my.monster.com/Privacy/Default.aspx">Privacy Policy</a>, <a title="terms of use" target="_blank" href="http://my.monster.com/Terms/Default.aspx">Terms of Use</a> and <a title="use of cookies" target="_blank" href="http://inside.monster.com/cookie-info/inside2.aspx">Use of Cookies</a>.
                            </div>
                </div>
            </div>
        </div>
    </div>
    <script language="javaScript" type="text/javascript">
        var displayedEvar = false;

        $(function() {



            if (typeof $.cookie('SSALR_NonModal_Interaction') === 'undefined') {

                $(window).scroll(function() {
                    var height = $(window).scrollTop();
                    if (height > parseInt(300)) {
                        $('#jsa-top.popup-widget').addClass('reveal');

                        if (!displayedEvar) {
                            _m.ATM.atCall("document", "o", "SSA Top", { "events.event50": "true", "eVar68": "%NonModal%Top%On%300%" });
                            displayedEvar = true;
                        }

                    } else {
                        $('#jsa-top.popup-widget').removeClass('reveal');
                    }
                });
            }


            $('#jsa-top.widget.popup-widget .popup-close-icon').click(function() {
                $('#jsa-top.widget.popup-widget').fadeOut(400);
                $.cookie('SSALR_NonModal_Interaction', 'true', { domain: '.monster.com', path: '/' });

                _m.ATM.atCall("document", "o", "SSA Top", { "events.event51": "true", "eVar68": "%NonModal%Top%On%300%" });
            });

            $('#jsa-top.widget.popup-widget .error-box-close-icon').click(function () {
                $('#jsa-top.widget.popup-widget').removeClass('error-state');
            });

            // To show success state
            $('#jsa-top.widget.popup-widget .emailButtonModalPopup').click(function () {
                $.cookie('SSALR_NonModal_Interaction', 'true', { domain: '.monster.com', path: '/' });
                emailActionModalPopupClick('You need to agree to our Privacy Policy, Terms of Use and Use of Cookies before continuing', "#jsa-top", Callback_SiteCatSSATop, this);
            });
        });

        function Callback_SiteCatSSATop() {

                _m.ATM.atCall("document", "o", "SSA Top", { "events.event26": "true", "eVar68": "%NonModal%Top%On%300%" });

        }
    </script>
    <style>
    </style>

                </div>


	                </div>
	                <!-- Main content ends -->
	            </div><!-- Matter ends -->
	        </div><!-- Mainbar ends -->
	    </div>
	    <div class="clearfix"></div>
	    <!-- Footer -->
        <!-- Footer starts -->


        <div class="bannerAdFooter hidden-xs">

        </div>



<input type="hidden" id="envType" value="Production" />
<input type="hidden" id="version" value="1.0.0.0" />


    <footer role="contentinfo" class="new-footer">
        <div class="container">
            <a class="m-logo" href="https://www.monster.com" title="Go to Monster home"><img alt="Monster logo" src="https://securemedia.newjobs.com/niche/images/niche-footer-m.gif" /></a>
        <!-- Desktop view -->
        <div class="row hidden-xs">
            <ul class="col-sm-2 clearfix">
                <li><h3>For Job Seekers</h3></li>
                <li><a href="https://www.monster.com/jobs/">Find Jobs</a></li>
                <li><a href="http://resume.monster.com">Upload Resume</a></li>
                <li><a href="https://www.monster.com/sitemap" title="Job Seeker Site Map">Site Map</a></li>
                <li><a onclick="window.open(this.href, 'pop', 'toolbar=no,directories=no,location=no,status=yes,menubar=no,resizable=yes,scrollbars=yes,width=995,height=575'); return false;" href='https://monster.secure.force.com/ekb/EKBHome?brand=seeker' title="Job Seeker Help">Help</a></li>
            </ul>
            <ul class="col-sm-2 clearfix">
                <li><h3>For Employers</h3></li>
                <li><a href="http://hiring.monster.com">Post Jobs</a></li>
                <li><a href="http://hiring.monster.com/recruitment/Resume-Search-Database.aspx">Search Resumes</a></li>
                <li><a href="http://advertising.monster.com/">Advertise with us</a></li>
                <li><a href="http://hiring.monster.com/sitemap.aspx" title="Employer Site Map">Site Map</a></li>
                <li><a onclick="window.open(this.href, 'pop', 'toolbar=no,directories=no,location=no,status=yes,menubar=no,resizable=yes,scrollbars=yes,width=995,height=575'); return false;" href='https://monster.secure.force.com/ekb/EKBHome?brand=monster_usen' title="Employer Help">Help</a></li>
            </ul>
            <ul class="col-sm-2 clearfix">
                <li><h3>About Us</h3></li>
                <li><a href="https://www.monster.com/about">About Monster</a></li>
                <li><a href="https://www.monster.com/about/work-for-us">Work for Monster</a></li>
                <li><a href="http://partner.monster.com/">Partner with Us</a></li>
                <li><a href="http://ir.monster.com/phoenix.zhtml?c=110723&amp;p=irol-irhome">Investor Relations</a></li>
                <li><a href="https://www.monster.com/geo/siteselection">Monster International</a></li>
            </ul>
            <ul class="col-sm-2 clearfix">
                <li><h3>Helpful Resources</h3></li>
                <li><a onclick="window.open(this.href, 'pop', 'toolbar=no,directories=no,location=no,status=yes,menubar=no,resizable=yes,scrollbars=yes,width=995,height=575'); return false;" href='https://monster.secure.force.com/ekb/EKBContactUs?brand=seeker' title="Contact Us Popup">Contact Us</a></li>
                <li><a href="http://inside.monster.com/terms-of-use">Terms of Use</a></li>
                <li><a href="http://inside.monster.com/privacy/home.aspx">Privacy Center</a></li>
                <li><a href="http://inside.monster.com/security-center/home.aspx">Security Center</a></li>
                <li><a href="http://inside.monster.com/accessibility">Accessibility Center</a></li>
                <li><a href="http://preferences.truste.com/2.0/?type=monster&amp;affiliateId=155" rel="nofollow">AdChoices <i class="iconAdChoices"></i></a></li>
            </ul>
            <ul class="col-sm-2 clearfix">
                <li><h3>Find Jobs</h3></li>
                <li><a href="https://www.monster.com/jobs/">Jobs in US</a></li>
                <li><a href="https://www.monster.ca/jobs/">Jobs in Canada</a></li>
                <li><a href="https://www.monster.co.uk/jobs/">Jobs in UK</a></li>
                <li><a href="https://www.monster.fr/emploi/">Emplois en France</a></li>
                <li><a href="https://www.monster.de/jobs/">Jobs in Deutschland </a></li>
                <li><a href="https://www.monsterboard.nl/vacatures/">Vacatures in Nederland</a></li>
            </ul>
        </div>
        <!-- Mobile view -->
        <div class="row visible-xs">
            <ul class="col-xs-12 clearfix">
                <li><a href="https://www.monster.com/jobs/">Find Jobs</a></li>
                <li><a href="http://hiring.monster.com">Post Jobs</a></li>
                <li><a href="https://www.monster.com/about">About Monster</a></li>
               <li><a onclick="window.open(this.href, 'pop', 'toolbar=no,directories=no,location=no,status=yes,menubar=no,resizable=yes,scrollbars=yes,width=681,height=1053'); return false;" href='https://monster.secure.force.com/ekb/EKBContactUs?brand=seeker' title="Contact Us Popup">Contact Us</a></li>
                <li><a href="http://inside.monster.com/terms-of-use">Terms of Use</a></li>
                <li><a href="http://inside.monster.com/privacy/home.aspx">Privacy Center</a></li>
                <li><a href="http://inside.monster.com/security-center/home.aspx">Security Center</a></li>
            </ul>
        </div>
        <div class="findSocial">
            <h3>Find us on <a href="http://career-services.monster.com/social-media/home.aspx">social media</a>:</h3>
            <a class="fa fa-google-plus" href="https://plus.google.com/+monster" target="_blank"><span class="sr-only">Google Plus</span></a>
            <a class="fa fa-facebook" href="https://www.facebook.com/monster" target="_blank"><span class="sr-only">Facebook</span></a>
            <a class="fa fa-twitter" href="https://twitter.com/Monster" target="_blank"><span class="sr-only">Twitter</span></a>
            <a class="fa fa-instagram" href="https://instagram.com/monster" target="_blank"><span class="sr-only">Instagram</span></a>
            <a class="fa fa-youtube" href="https://www.youtube.com/monster" target="_blank"><span class="sr-only">YouTube</span></a>
        </div>
        <p class="copyrights">
            Copyright &copy; 2016 - <a href="https://www.monster.com/">Monster Worldwide</a>
        </p>
        <p class="patents">
            <span class="hidden-xs">U.S. Patents No. 7,599,930 B1; 7,827,125 and 7,836,060 - </span>Looking for <a href="http://www.monsterproducts.com/" target="_blank" rel="nofollow">Monster Cable</a>?
         - V: 2017.7.0.16-303</p>

        </div>
    </footer>



        <!-- Footer ends -->
    </div>
    <!-- Scroll to top -->
    <span class="totop"><a href="#"><i class="fa fa-chevron-up"></i></a></span>
    <div class="hide">



<div style="display:none;"></div>












    </div>
   </body>
</html>
"""

html_40 ="""

<!DOCTYPE html>
<html xmlns="https://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>


    <meta http-equiv="X-UA-Compatible" content="IE=8, IE=9, IE=10" />
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta http-equiv="Expires" content="0" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1" />
<meta charset="utf-8">
<link type="text/css" rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500">


<!--[if IE 8]>
      <link rel="stylesheet" type="text/css" href="https://securemedia.newjobs.com/niche/css/generic-template/style-ie.css" />
<![endif]-->

<!--[if lt IE 9]>
<script src="https://securemedia.newjobs.com/niche/js/html5shim.js"></script>
<script src="/siteassets/scripts/respond.js" type="text/javascript"></script>
<![endif]-->

    <script src="https://oas.monster.com/Scripts/oas_analytics.js" type="text/javascript"></script>


<title>Python Jobs | Monster.com - Page 40</title>
    <link rel="canonical" href="https://www.monster.com/jobs/q-python-jobs.aspx?page=40" />
<link id="favIcon" runat="server" rel="shortcut icon" href="https://securemedia.newjobs.com/favicon.ico" />
<meta name="description" content="Explore more than 1,000 Python jobs in the United-States. Browse by location or industry. Find the right position and build your career.- Page 40" />
<meta name="keywords" content="Python jobs, Python career resources, Python careers, Python job, Python career, Python employment, Python work, Python job opportunities, Python employment opportunities, jobs in Python, careers in Python" />
<meta name="SL.domain" content = "login.monster.com" />
<meta name="SL.channelAlias" content="MONS" />
    <meta content="Python Jobs | Monster.com - Page 40" property="og:title" />
    <meta content="website" property="og:type" />
    <meta content="https://www.monster.com/jobs/search/?q=Python&amp;page=40" property="og:url" />
    <meta content="https://securemedia.newjobs.com/id/lpf20/CORE/icon-50-m.png" property="og:image" />
    <meta content="Monster" property="og:site_name" />
    <meta content="Explore more than 1,000 Python jobs in the United-States. Browse by location or industry. Find the right position and build your career.- Page 40" property="og:description" />
    <meta content="Python Jobs | Monster.com - Page 40" itemprop="name" />
    <meta content="Explore more than 1,000 Python jobs in the United-States. Browse by location or industry. Find the right position and build your career.- Page 40" itemprop="description" />
    <meta content="https://securemedia.newjobs.com/id/lpf20/CORE/icon-50-m.png"  itemprop="image" />
    <link rel="prev" href="https://www.monster.com/jobs/search/?q=Python&amp;page=39" />
    <link href="https://css-seeker.newjobs.com/MONS/v4.1.2.8/lpf30.v2_css.axd?s=1" type="text/css" rel="stylesheet" />
    <script type="text/javascript" src="https://js-seeker.newjobs.com/MONS/v4.1.2.34/lpf30_js.axd?s=1"></script>







<meta content="Monster" name="m_impr.a_affiliate_id" /><meta content="q=Python&amp;brd=1&amp;brd=2&amp;cy=US&amp;pg=40&amp;pp=25&amp;sort=rv.di.dt&amp;stp=TwoBoxBand" name="m_impr.s_search_query" />
<meta content="Python" name="m_impr.s_q" />
<meta content="40" name="m_impr.j_pg" />











<script type="text/javascript" src="//nexus.ensighten.com/monster/Bootstrap.js"></script>



<meta name="debugInfo" content="
"/>

    <script type="text/javascript">
       var inHeadTS = (new Date()).getTime();
    </script>
        <script type="text/javascript">
        var navResult = {"Result":{"ChannelId":58,"ChannelAlias":"MONS","NavHeader":null,"NavFooter":null},"Status":"Success","ErrorDetails":"Success","ErrorGuid":""};
        if (navResult.Result.NavHeader != null) {
            document.write ("<link rel='stylesheet' type='text/css' href='https://securemedia.newjobs.com/global/css/www/newspaper-nav/newspaper-nav.css' />");
            document.write("<style>.mainbar .matter{margin-top: 0;} .logo-newspaper {background: url('" + navResult.Result.NavHeader.NpLogoImageUrl + "') no-repeat scroll center center / contain} .jobAlertButton {top:112px} @media (max-width: 767px) { .logo-newspaper {height: 50px; margin-left:0;} .navbar.solid-nav .navbar-text.login-btn {margin-top: 8px;} .navbar .navbar-toggle.search-btn-container {margin: 7px 0 0;} body {margin-top: 146px !important;} .jobAlertButton {top: 120px;} }</style>");
        }
    </script>

</head>
<body class="card-view-2">
<script type="text/javascript" language="javascript">var DYNAMIC_S_ACCOUNT='newjobsProdSeekerUS';var DYNAMIC_S_CURRENCYCODE='USD';</script><script type="text/javascript">//<![CDATA[
var amc=amc||{};if(!amc.on){amc.on=amc.call=function(){}};
document.write("<scr"+"ipt type='text/javascript' src='https://securemedia.newjobs.com/js/sc/targetsitecatalystloadtimeLL.js'></sc"+"ript>");
//]]>
_m.ATM.properties={"eVar2":"unrecognized","channel":"58","eVar1":"D=g","prop1":"D=g","eVar4":"0","eVar17":"Unspecified","eVar16":"trovix-cloud-band","eVar23":"1001+","eVar19":"Python","eVar24":"40","eVar18":"Unspecified","events.event1":"jobsearch","eVar20":"Unspecified","list2":"Unspecified","list1":"Unspecified","eVar21":"Unspecified","prop16":"Unspecified","prop17":"Unspecified","prop18":"Unspecified","prop19":"Unspecified","eVar22":"Unspecified","events.event27":"true","eVar69":"NewCardView","list3":"ViewSplit_NewCardView,BAMLiteSplit_Default,TypeaheadElasticSearchSplit_NewElasticSearch","eVar43":"Cloud Search Y"};_m.ATM.pageName='desktop|mons|lpf|jobsearch-trovix-cloud-band';_m.ATM.version=0;_m.ATM.appID='lpf';_m.ATM.channelID=58;_m.ATM.countryID=164;_m.ATM.appConfig={version:'0',appID:'lpf',channelID:'58',countryID:'164'};_m.ATM.runOnLoad=true;
(function () {if (typeof _m.ATM.initFromOnReady === 'function') {_m.ATM.initFromOnReady();} else {setTimeout(function () {if (typeof _m.ATM.initFromOnReady === 'function') {_m.ATM.initFromOnReady();} else {$(document).ready(_m.ATM.initFromOnReady);}}, 200);}})();</script>


<!-- Google Tag Manager -->
<noscript><iframe src="//www.googletagmanager.com/ns.html?id=GTM-NQK2FJ"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-NQK2FJ');</script>
<!-- End Google Tag Manager -->



<div style="display:none;"></div>

    <!-- start of markup for nano ad -->

    <script type="text/javascript" language="JavaScript">
        $(function () {
            _s.lpf.canTrack.trackI();
        });
    </script>

<!-- end of markup for nano ad -->


<a href="#mainContent" class="skip-main">Skip to main content</a>








    <div id="headerWidget">


<input type="hidden" id="AcceptCookies" value="True" />

<input type="hidden" id="lpfDomainPath" value="https://www.monster.com/jobs" />
<input type="hidden" id="servicesDomainPath" value="https://www.monster.com/jobs" />
<input type="hidden" id="inboxLink" value="https://www.monster.com/message/inbox" />
<input type="hidden" id="countryId" value="164" />
<input type="hidden" id="showLocationTypeAheadTrovix" value="True" />
<input type="hidden" id="showLocationTypeAheadLucene" value="False" />
<input type="hidden" id="showKeywordTypeAheadTrovix" value="True" />
<input type="hidden" id="isLoggedIn" value="False" />
<input type="hidden" id="isOnlyRecognized" value="False" />
<input type="hidden" id="successMessage" value="You have no new messages." />
<input type="hidden" id="cookieName" value="hdCookiesIM" />
<input type="hidden" id="cookieValue" value="0" />
<input type="hidden" id="cookieExpirationTime" value="365" />
<input type="hidden" id="cookieDomain" value=".monster.com" />
<input type="hidden" id="searchPageAction" value="https://www.monster.com/jobs/search/" />
<input type="hidden" id="mcMainBox" class="mc-mail-box" value="" />
<input type="hidden" id="mcAwsUrl" value="" />

<input type="hidden" id="countryCode" value="US" />
<input type="hidden" id="languageCode" value="EN" />
<input type="hidden" id="typeAheadRequestUrl" value="https://c6v0t0t861.execute-api.us-east-1.amazonaws.com/Prod/vulcantypeaheadresource?matchString=%Q&amp;countrycode={0}&amp;languagecode={1}&amp;fuzziness=0" />
<input type="hidden" id="esTypeaheadEnabled" value="True" />
<input type="hidden" id="msgKeywords" value="Key Words" />
<input type="hidden" id="msgJobTitles" value="Job Titles" />
<input type="hidden" id="msgCompanyNames" value="Company Names" />

<div id="pv_nav-fixed">
    <!-- Top Nav -->
    <nav class="solid-nav navbar-2 navbar navbar-default navbar-fixed-top" role="navigation" id="jsrHeader">
        <div style="display: none" class="interMsgsW cookie-msg">
            <div class="interMsgsPar">
                <div class="interMsg">
                    <a onclick="return false;" name="closeIMEmployer" href="#" class="close-msg" title="Don&#39;t display this message again">
                        <span class="dontDisplay">Don&#39;t display this message again</span>
                        <span class="counter"></span><span class="fa fa-times"></span>
                    </a>
                    <h4>A Note About Cookies</h4>

                </div>
            </div>
        </div>
        <div class="container-fluid navbar-main">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <a class="navbar-brand" href="https://www.monster.com" aria-label="Monster Home">
                    <div class="logo">&nbsp;</div>
                </a>
                <!-- End Monster Logo -->
                <!-- Buttons in reverse order for Bootstrap -->
                <!-- New "Trigger" classes on buttons for JS (transitions.closeDropdowns()) -->
                <button type="button" class="navbar-toggle nav-trigger action action--open" aria-label="Open Menu">
                    <span class="sr-only">Toggle Navigation Mobile</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <!-- End Hamburger Button -->
                <button type="button" class="navbar-toggle navbar-toggle-account account-trigger action action--open-2 hidden-sm hidden-md hidden-lg" aria-label="Open Menu">
                    <span class="sr-only">Toggle Account Navigation</span>
                        <span class="navbar-profile-icon center-block"></span>
                    <span class="emailCount"></span>
                    <span class="logged-name">Account</span>
                </button>
                <!-- End Account Button -->
                <button type="button" class="navbar-toggle search-btn-container search-trigger" data-toggle="collapse" data-target="#mobile-navbar-search" aria-expanded="false">
                    <i class="fa fa-search"></i>
                    <span class="navbar-text">Jobs</span>
                </button>
                <!-- End Search Button -->
            </div>
            <!-- End Mobile Header/Navbar -->
            <div class="collapse navbar-collapse text-center" id="mobile-navbar-search" style="max-height: 423px;">
                <!-- End Navbar Right, Login, Signup, & Employer Links -->
                <form id="quickJobSearch" role="search" class="navbar-form" method="get">
                    <div class="form-group top-search keywords">
                        <label for="keywords" class="sr-only">Keywords</label>
                        <div class="input-group input-group-sm">
                            <span class="input-group-addon"><i class="zmdi zmdi-search"></i></span>
                                <div id="multiple-datasets">
                                    <input type="text" class="form-control typeaheadR tt-hint hasclear" placeholder="Search for Jobs" id="keywords2" name="q" value="Python" />
                                    <input type="hidden" id="typeaheadvalues" value="" />
                                </div>
                            <span class="input-clear" style="">x</span>
                        </div>
                    </div>
                    <div class="form-group top-search location">
                        <label for="location" class="sr-only">Location</label>
                        <div class="input-group input-group-sm">
                            <span class="input-group-addon"><i class="zmdi zmdi-pin"></i></span>
                            <input type="text" autocomplete="off" id="location" name="where" class="form-control input-sm typeahead hasclear" placeholder="Location" value="" />
                            <span class="input-clear" style="">x</span>
                        </div>
                    </div>
                    <button onclick="InitializeGlobalheaderSearch(); return false;" class="btn btn-white btn-sm" type="button" id="doQuickSearch">Search</button>
                        <div class="tm-wrap">
                            <input class="tm-input hidden" type="hidden" maxlength="200" />
                        </div>
                </form>

                <!-- End Search Form (Desktop & Mobile) -->
                <ul class="nav navbar-nav navbar-right hidden-xs">
                    <li class="dropdown account-dropdown">
                        <a href="#" class="dropdown-toggle navbar-icon-link loginLink2" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
                            <span class="sr-only">Toggle Account Navigation</span>
                                <span class="navbar-profile-icon center-block"></span>
                            <span class="emailCount"></span>
                            <span>Account</span>
                        </a>
                        <ul class="dropdown-menu">
                                <li>
                                    <a href="https://login20.monster.com/?r=https%3a%2f%2fwww.monster.com%2fjobs%2fsearch%2f%3fq%3dPython%26page%3d40&amp;ch=MONS" title="Log In" gfltrack="1" >Log In</a>
                                </li>
                                <li>
                                    <a href="https://login20.monster.com/Become-Member/Create-Account?r=https%3a%2f%2fwww.monster.com%2fjobs%2fsearch%2f%3fq%3dPython%26page%3d40&amp;landedFrom=Header&amp;ch=MONS" title="Sign Up" gfltrack="1" >Sign Up</a>
                                </li>
                        </ul>
                    </li>
                        <li>
                            <div id="login-btn-employer">
                                <a href="http://hiring.monster.com/?intcid=skr_LPF_TopNav_Employer" title="Employers: Post Jobs and Find Talent">
                                    Employers<br>
                                    <span>Post Jobs &amp; Find Talent </span>
                                </a>
                            </div>
                        </li>
                </ul>
            </div>
        </div>
        <div class="container-fluid subnav top-subnav hidden-xs">
            <ul class="nav navbar-nav hidden-xs subnav-nav clearfix">
                        <li id="main-nav-0" class="dropdown">
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
                                Find Jobs <span class="caret"></span>
                            </a>
                            <ul class="dropdown-menu">

            <li id="sub-nav-0">
                <a href="https://www.monster.com/jobs/advanced-search">Advanced Search</a>
            </li>
            <li id="sub-nav-1">
                <a href="https://www.monster.com/jobs/">Browse Jobs</a>
            </li>
<div class="cmsNavContainer componentDC1">
<h3 class="fnt5">Most Popular Jobs</h3>

<ul>
	<li><a href="https://www.monster.com/jobs/q-courier-jobs.aspx" title="Courier Jobsg">Courier Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-delivery-driver-jobs.aspx" title="Delivery Driver Jobs">Delivery Driver Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-dental-assistant-jobs.aspx" title="Dental Assistant Jobs">Dental Assistant Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-electrician-jobs.aspx" title="Electrician Jobs">Electrician Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-medical-assistant-jobs.aspx" title="Medical Assistant Jobs">Medical Assistant Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-truck-driver-jobs.aspx" title="Truck Driver Jobs">Truck Driver Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-pharmacist-jobs.aspx" title="Pharmacist Jobs">Pharmacist Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-pharmacy-technician-jobs.aspx" title="Pharmacy Technician Jobs">Pharmacy Technician Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-receptionist-jobs.aspx" title="Receptionist Jobs">Receptionist Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-security-guard-jobs.aspx" title="Security Guard Jobs">Security Guard Jobs</a></li>
</ul>
</div>

                            </ul>
                        </li>
                        <li id="main-nav-1" class="dropdown">
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
                                Career Resources <span class="caret"></span>
                            </a>
                            <ul class="dropdown-menu">

            <li id="sub-nav-2">
                <a href="https://www.monster.com/career-advice">Career Advice</a>
            </li>
            <li id="sub-nav-3">
                <a href="http://career-services.monster.com/">Career Services</a>
            </li>
            <li id="sub-nav-4">
                <a href="https://www.monster.com/communities">Communities</a>
            </li>
            <li id="sub-nav-5">
                <a href="https://www.monster.com/news">Employment News</a>
            </li>
<div class="cmsNavContainer componentDC2">
<h3 class="fnt5">Additional Resources</h3>

<ul>
	<li><a class="ext" href="https://www.topresume.com/resume-writing/?pt=eTBKg0FP8WHu&amp;por=monster&amp;utm_medium=referral&amp;utm_source=Monster+TopResume&amp;utm_content=Resume_CareerResources_RWS" title="Resume Writing Services">Resume Writing Services</a></li>
	<li><a class="ext" href="https://www.monster.com/career-advice/cover-letter-resume" title="Resume Advice">Resume Advice</a></li>
	<li><a class="ext" href="https://www.monster.com/career-advice/job-interview" title="Interviewing Tips
    ">Interviewing Tips</a></li>
	<li><a href="https://www.monster.com/personal-finance-center" title="Personal Finance Center">Personal Finance Center</a></li>
	<li><a href="https://www.monster.com/career-advice/salary-benefits" title="Salary &amp; Benefits">Salary &amp; Benefits</a></li>
	<li><a class="ext" href="https://www.monster.com/career-advice/article/industry-career-advice" title="Career Advice by Industry">Career Advice by Industry</a></li>
	<li><a href="https://www.monster.com/career-advice/professional-development/education-training" title="Education &amp; Training">Education &amp; Training</a></li>
	<li><a href="https://www.monster.com/blog" target="">Monster Blog</a></li>
	<li><a href="http://resources.monster.com/diversity-inclusion/work/" title="Diversity Resources">Diversity Resources</a></li>
</ul>
</div>

                            </ul>
                        </li>
                        <li id="main-nav-2">
                            <a href="https://www.monster.com/resumes/post-resume?landedFrom=Header">Post a Resume
</a>
                        </li>
                        <li id="main-nav-3">
                            <a href="https://www.monster.com/company">Company Profiles</a>
                        </li>
            </ul>

        </div>
        <!-- End Main Nav or "Subnav" (Desktop)-->
        <!-- Slideout Menu Container -->
        <div class="container">
            <!-- Menu -->
            <nav id="ml-menu-2" class="menu">
                <!-- Close button for mobile version -->
                <button class="action action--close-2" aria-label="Close Menu">×</button>
                <div class="menu__wrap">
                    <ul data-menu="main" class="menu__level menu__level--current">
                            <li class="menu__item">
                                <a class="menu__link" href="https://login20.monster.com/?r=https%3a%2f%2fwww.monster.com%2fjobs%2fsearch%2f%3fq%3dPython%26page%3d40&amp;ch=MONS" title="Log In" gfltrack="1" >Log In</a>
                            </li>
                            <li class="menu__item">
                                <a class="menu__link" href="https://login20.monster.com/Become-Member/Create-Account?r=https%3a%2f%2fwww.monster.com%2fjobs%2fsearch%2f%3fq%3dPython%26page%3d40&amp;landedFrom=Header&amp;ch=MONS" title="Sign Up" gfltrack="1" >Sign Up</a>
                            </li>
                    </ul>
                </div>
            </nav>
        </div>
        <!-- End Main Container for Mobile Main Nav -->
        <!-- Main container -->
        <div class="container">
            <!-- Menu -->
            <!-- Mobile Left Nav -->
            <nav id="ml-menu" class="menu">
                <!-- Close button for mobile version -->
                <button class="action action--close" aria-label="Close Menu">×</button>
                <!-- Edit contents of Init Crumb 1 to edit first breadcrumb in left slidout menu. -->
                <span id="init-crumb-1" style="display: none; visibility: hidden;">all</span>
                <!-- Menu contents. -->
                <div id="ml-menu-container" class="menu__wrap">
                    <ul data-menu="main" class="menu__level menu__level--current">
                        <li id="mobile-nav-home" class="menu__item">
                                <a class="menu__link" href="https://www.monster.com">Home</a>
                        </li>
                                <li id="mobile-nav-0" class="menu__item">
                                    <a class="menu__link" data-submenu="submenu-0" href="#">Find Jobs</a>
                                    <ul data-menu="submenu-0" class="menu__level">

    <li id="mobile-subnav-0" class="menu__item">
        <a class="menu__link" href="https://www.monster.com/jobs/advanced-search">Advanced Search</a>
    </li>
    <li id="mobile-subnav-1" class="menu__item">
        <a class="menu__link" href="https://www.monster.com/jobs/">Browse Jobs</a>
    </li>
    <li id="mobile-subnav-" class="menu__item">
        <a class="menu__link" data-submenu="submenu-cms-109" href="#"></a>
        <ul data-menu="submenu-cms-109" data-sub-for="109" class="menu__level cms-submenu">
            <div class="cmsNavContainer componentDC1">
<h3 class="fnt5">Most Popular Jobs</h3>

<ul>
	<li><a href="https://www.monster.com/jobs/q-courier-jobs.aspx" title="Courier Jobsg">Courier Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-delivery-driver-jobs.aspx" title="Delivery Driver Jobs">Delivery Driver Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-dental-assistant-jobs.aspx" title="Dental Assistant Jobs">Dental Assistant Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-electrician-jobs.aspx" title="Electrician Jobs">Electrician Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-medical-assistant-jobs.aspx" title="Medical Assistant Jobs">Medical Assistant Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-truck-driver-jobs.aspx" title="Truck Driver Jobs">Truck Driver Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-pharmacist-jobs.aspx" title="Pharmacist Jobs">Pharmacist Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-pharmacy-technician-jobs.aspx" title="Pharmacy Technician Jobs">Pharmacy Technician Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-receptionist-jobs.aspx" title="Receptionist Jobs">Receptionist Jobs</a></li>
	<li><a href="https://www.monster.com/jobs/q-security-guard-jobs.aspx" title="Security Guard Jobs">Security Guard Jobs</a></li>
</ul>
</div>

        </ul>
    </li>

                                    </ul>
                                </li>
                                <li id="mobile-nav-1" class="menu__item">
                                    <a class="menu__link" data-submenu="submenu-1" href="#">Career Resources</a>
                                    <ul data-menu="submenu-1" class="menu__level">

    <li id="mobile-subnav-2" class="menu__item">
        <a class="menu__link" href="https://www.monster.com/career-advice">Career Advice</a>
    </li>
    <li id="mobile-subnav-3" class="menu__item">
        <a class="menu__link" href="http://career-services.monster.com/">Career Services</a>
    </li>
    <li id="mobile-subnav-4" class="menu__item">
        <a class="menu__link" href="https://www.monster.com/communities">Communities</a>
    </li>
    <li id="mobile-subnav-5" class="menu__item">
        <a class="menu__link" href="https://www.monster.com/news">Employment News</a>
    </li>
    <li id="mobile-subnav-" class="menu__item">
        <a class="menu__link" data-submenu="submenu-cms-165" href="#"></a>
        <ul data-menu="submenu-cms-165" data-sub-for="165" class="menu__level cms-submenu">
            <div class="cmsNavContainer componentDC2">
<h3 class="fnt5">Additional Resources</h3>

<ul>
	<li><a class="ext" href="https://www.topresume.com/resume-writing/?pt=eTBKg0FP8WHu&amp;por=monster&amp;utm_medium=referral&amp;utm_source=Monster+TopResume&amp;utm_content=Resume_CareerResources_RWS" title="Resume Writing Services">Resume Writing Services</a></li>
	<li><a class="ext" href="https://www.monster.com/career-advice/cover-letter-resume" title="Resume Advice">Resume Advice</a></li>
	<li><a class="ext" href="https://www.monster.com/career-advice/job-interview" title="Interviewing Tips
    ">Interviewing Tips</a></li>
	<li><a href="https://www.monster.com/personal-finance-center" title="Personal Finance Center">Personal Finance Center</a></li>
	<li><a href="https://www.monster.com/career-advice/salary-benefits" title="Salary &amp; Benefits">Salary &amp; Benefits</a></li>
	<li><a class="ext" href="https://www.monster.com/career-advice/article/industry-career-advice" title="Career Advice by Industry">Career Advice by Industry</a></li>
	<li><a href="https://www.monster.com/career-advice/professional-development/education-training" title="Education &amp; Training">Education &amp; Training</a></li>
	<li><a href="https://www.monster.com/blog" target="">Monster Blog</a></li>
	<li><a href="http://resources.monster.com/diversity-inclusion/work/" title="Diversity Resources">Diversity Resources</a></li>
</ul>
</div>

        </ul>
    </li>

                                    </ul>
                                </li>
                                <li id="mobile-nav-2" class="menu__item">
                                    <a class="menu__link" href="https://www.monster.com/resumes/post-resume?landedFrom=Header">Post a Resume
</a>
                                </li>
                                <li id="mobile-nav-3" class="menu__item">
                                    <a class="menu__link" href="https://www.monster.com/company">Company Profiles</a>
                                </li>


                    </ul>
                </div>
            </nav>
        </div>
        <!-- End Main Container for Mobile Main Nav -->

    </nav>
    <!-- End Navbar Fixed Top -->

    <!-- Nav Modal End -->
</div>




<script type="text/javascript">

    $(function () {
        //Sub-Menu Mobile
        var $mlSubMenus = $('#ml-menu-container ul[data-menu*="submenu-"]');
        if ($mlSubMenus.length) {
            $mlSubMenus.each(function () {
                $(this).appendTo('#ml-menu-container');
            });
        }

        //CMS Desktop
        var $cmsNavContainers = $("li[id*='main-nav-'] div.cmsNavContainer");
        if ($cmsNavContainers.length) {
            for (var i = 0; i < $cmsNavContainers.length; i++) {
                var $this = $($cmsNavContainers[i]);
                $this.addClass('hidden');
                var title = $this.find('h3').html();
                var $childs = $this.find('ul li');

                var $parentUl = $this.closest('ul');
                $parentUl.append('<li class="cmsNavContainer dropdown-sub"></li>');
                var $newCmsContainer = $parentUl.find('li.cmsNavContainer.dropdown-sub');
                $newCmsContainer.append('<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">' + title + ' <span class="caret"></span></a>');
                $newCmsContainer.append('<ul class="dropdown-menu dropdown-menu-sub"></ul>');
                $newCmsContainer.find('ul').append($childs);

                $this.remove();
            }
        }

        //CMS Mobile
        var $mobileCmsNavContainers = $("#ml-menu-container ul.cms-submenu div.cmsNavContainer");
        if ($mobileCmsNavContainers.length) {
            for (var i = 0; i < $mobileCmsNavContainers.length; i++) {
                var $this = $($mobileCmsNavContainers[i]);
                var $parentUl = $this.closest('ul.cms-submenu');

                $this.addClass('hidden');
                var thisTitle = $this.find('h3').html();
                var $thisChilds = $this.find('ul li');

                var dataMenu = $parentUl.attr('data-menu');
                var dataSubFor = $parentUl.attr('data-sub-for');

                $thisChilds.each(function () {
                    $(this).addClass('menu__item');
                    $(this).find('a').addClass('menu__link');
                });

                $thisChilds.appendTo($parentUl);
                $this.remove();

                var $subLinkAnchor = $("#ml-menu-container a.menu__link[data-submenu='submenu-cms-" + dataSubFor + "']");
                if ($subLinkAnchor.length) {
                    $subLinkAnchor.html(thisTitle);
                }
            }
        }

        setTimeout(function () {
            globalHeaderNavigation({"InitialBreadcrumbText":"all"});
        }, 300);
    });

    $(document).ready(function () {
        var isUsingAppDomainForServices = false;
        if ('False' === 'True') {
            isUsingAppDomainForServices = true;
        }

        InitializeHeaderBarJsr(isUsingAppDomainForServices); // all header related script
    });
</script>


    </div>


    <div class="wrap jsrMain">
	    <div class="content" id="jsr">
  		    <span class="anchor" id="mainContent"></span>
	        <div class="mainbar">
	            <div class="matter">



<style>
    .containerdebug .contentdebug {
        padding : 5px;
        background-color: #f7e7bd;
    }
    .containerdebug {
        border:1px solid #748649;
        word-wrap: break-word;
        padding: 0;
    }
    .containerdebug div {
        width:100%;
    }
    .containerdebug .headerdebug {
        background-color:#d3d3d3;
        padding: 2px;
        cursor: pointer;
        font-weight: bold;
    }
</style>





	                <!-- Main content starts -->
	                <div class="container">

    <div class="row">


    </div>
    <div class="row">
        <div class="col-sm-4 col-lg-3 hidden-xs jsr-left-rail" xmlns:ms="urn:schemas-microsoft-com:xslt" xmlns:ContentBlockManager="urn:content-block-manager" xmlns:WidgetManager="urn:widget-manager" xmlns:FormatUtils="urn:format-utils">


<input type="hidden" id="isDynamicResult" value="True" />

<input type="hidden" id="showNewJobs" value="False" />
<input type="hidden" id="enableNewJobsCount" value="False" />
<input type="hidden" id="lpfUrl" value="https://www.monster.com/jobs" />

<script type="text/javascript">
    $(document).ready(function () {

        InitializeNewJobsCount();

        $('[data-toggle="tooltip"]').tooltip();

        $('.jsr-left-rail .recent-searches-container .label').hover(function () {
            $(this).addClass('show-details');
        });

        $('.jsr-left-rail .recent-searches-container .label').mouseleave(function () {
            $(this).removeClass('show-details');
        });
    });
</script><div class="filterHeader">Filter Results By:</div>
<div class="refine">



     <div class="refine-section">
        <h4>Sort By:</h4>
        <div class="btn-group" role="group">
            <button class="btn btn-default sort-by-btn active" type="button"  onclick="setGetParameter('sort', 'rv.dt.di'); triggerFilterClick(null, 'sort', 'rv.dt.di');">Relevance</button>
            <button class="btn btn-default sort-by-btn " type="button" onclick="setGetParameter('sort', 'dt.rv.di'); triggerFilterClick(null, 'sort', 'dt.rv.di');">Date</button>
        </div>
    </div>
    <script type="text/javascript">
        $(document).ready(function () {
            $("button[class^='btn btn-default sort-by-btn']").on('click', function () {
                $(this).addClass('active');
            });
        });
    </script>

    <div class="refine-section">
        <h4>Company Search:</h4>
        <div class="form-group">
            <label class="sr-only" for="coSearch">Company Search</label>
            <input class="form-control" placeholder="Enter company name" aria-label="Company Search:" id="coSearch">
            <input id="companySearchUrl" type="hidden" value="https://www.monster.com/jobs/search/ZZcompanySearchZZ_6?q=Python">
        </div>
    </div>
    <script type="text/javascript">
        $(function () {
            InitializeCompanySearch();
        });
    </script>

<input type="hidden" id="evar63Json" value='{&quot;company&quot;: [&quot;&quot;],&quot;category&quot;: [&quot;&quot;],&quot;kywdjobtitle&quot;: [&quot;Python&quot;],&quot;location&quot;: [&quot;&quot;],&quot;skill&quot;: [&quot;&quot;],&quot;jobstatus&quot;: [&quot;&quot;],&quot;radius&quot;: [&quot;&quot;],&quot;sort&quot;: [&quot;&quot;]}' />

     <div class="refine-section">
         <h4>Job Status:</h4>
         <ul class="list">
                <li class="list__item">
                    <label class="label--checkbox">
                        <input type="checkbox" class="checkbox" disabled="disabled"    onclick="checkboxActionJobStatus(this, 'jobstatus', 'Full Time', 'https://www.monster.com/jobs/search/Full-Time_8?q=Python',  '')"/>
                        <span class="label--checkbox--span">Full Time</span>
                    </label>
                </li>
                <li class="list__item">
                    <label class="label--checkbox">
                        <input type="checkbox" class="checkbox" disabled="disabled"    onclick="checkboxActionJobStatus(this, 'jobstatus', 'Part Time', 'https://www.monster.com/jobs/search/Part-Time_8?q=Python',  '')"/>
                        <span class="label--checkbox--span">Part Time</span>
                    </label>
                </li>

         </ul>
    </div>
<script type="text/javascript">
       $("input.checkbox").removeAttr("disabled");

 </script>

</div>


    <div class="span3 menucontainer">
        <ul class="nav">
                            <li id="backlinkingwidgetSkill">
                                <h4>Skills:</h4>
                                <ul data-facettype="ft6" data-facetsearchparam="ftsp6" id="catdiv6" class="nav submenu" style="display: block;" aria-label="Skills:">
                                        <li onclick="triggerFilterClick(this, 'skill')"><a href="https://www.monster.com/jobs/search/?q=Python&amp;kwdv=1105" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Python Programming/Scripting Language">Python Programming/Scripting Language</a></li>
                                        <li onclick="triggerFilterClick(this, 'skill')"><a href="https://www.monster.com/jobs/search/?q=Python&amp;kwdv=713" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Java">Java</a></li>
                                        <li onclick="triggerFilterClick(this, 'skill')"><a href="https://www.monster.com/jobs/search/?q=Python&amp;kwdv=1075" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Scripting (Scripting Languages)">Scripting (Scripting Languages)</a></li>
                                        <li onclick="triggerFilterClick(this, 'skill')"><a href="https://www.monster.com/jobs/search/?q=Python&amp;kwdv=303" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Software Engineering">Software Engineering</a></li>
                                        <li onclick="triggerFilterClick(this, 'skill')"><a href="https://www.monster.com/jobs/search/?q=Python&amp;kwdv=1860" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Linux Operating System">Linux Operating System</a></li>
                                        <li id="showmoreSkillButton" class="showmorebutton">
                                            <a onclick="$('#showmoreSkillButton').hide();$('.showmoreSkillLinks').show();$('#showlessSkillButton').show();">Show More <span class="mdi mdi-chevron-down"></span></a>
                                        </li>
                                                <li onclick="triggerFilterClick(this, 'skill')" class="showmoreSkillLinks"><a href="https://www.monster.com/jobs/search/?q=Python&amp;kwdv=2014" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Perl Programming Language">Perl Programming Language</a></li>
                                                <li onclick="triggerFilterClick(this, 'skill')" class="showmoreSkillLinks"><a href="https://www.monster.com/jobs/search/?q=Python&amp;kwdv=1163" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="C++ Programming Language">C++ Programming Language</a></li>
                                                <li onclick="triggerFilterClick(this, 'skill')" class="showmoreSkillLinks"><a href="https://www.monster.com/jobs/search/?q=Python&amp;kwdv=1158" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="C Programming Language">C Programming Language</a></li>
                                                <li onclick="triggerFilterClick(this, 'skill')" class="showmoreSkillLinks"><a href="https://www.monster.com/jobs/search/?q=Python&amp;kwdv=1072" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="SQL (Structured Query Language)">SQL (Structured Query Language)</a></li>
                                                <li onclick="triggerFilterClick(this, 'skill')" class="showmoreSkillLinks"><a href="https://www.monster.com/jobs/search/?q=Python&amp;kwdv=2193" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="JavaScript">JavaScript</a></li>
                                        <li id="showlessSkillButton" class="showlessButton">
                                            <a onclick="$('#showlessSkillButton').hide();$('.showmoreSkillLinks').hide();$('#showmoreSkillButton').show();">Show Less <span class="mdi mdi-chevron-up"></span></a>
                                        </li>
                                </ul>
                            </li>
                            <li id="backlinkingwidgetCity">
                                <h4>City:</h4>
                                <ul data-facettype="ft2" data-facetsearchparam="ftsp2" id="catdiv2" class="nav submenu" style="display: block;" aria-label="City:">
                                        <li onclick="triggerFilterClick(this, 'location')"><a href="https://www.monster.com/jobs/search/?q=Python&amp;where=New-York__2c-NY" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL City Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="New York, NY">New York</a></li>
                                        <li onclick="triggerFilterClick(this, 'location')"><a href="https://www.monster.com/jobs/search/?q=Python&amp;where=Seattle__2c-WA" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL City Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Seattle, WA">Seattle</a></li>
                                        <li onclick="triggerFilterClick(this, 'location')"><a href="https://www.monster.com/jobs/search/?q=Python&amp;where=San-Francisco__2c-CA" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL City Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="San Francisco, CA">San Francisco</a></li>
                                        <li onclick="triggerFilterClick(this, 'location')"><a href="https://www.monster.com/jobs/search/?q=Python&amp;where=Santa-Clara__2c-CA" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL City Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Santa Clara, CA">Santa Clara</a></li>
                                        <li onclick="triggerFilterClick(this, 'location')"><a href="https://www.monster.com/jobs/search/?q=Python&amp;where=Chicago__2c-IL" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL City Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Chicago, IL">Chicago</a></li>
                                        <li id="showmoreCityButton" class="showmorebutton">
                                            <a onclick="$('#showmoreCityButton').hide();$('.showmoreCityLinks').show();$('#showlessCityButton').show();dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL City Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});">Show More <span class="mdi mdi-chevron-down"></span></a>
                                        </li>
                                                <li onclick="triggerFilterClick(this, 'location')" class="showmoreCityLinks"><a href="https://www.monster.com/jobs/search/?q=Python&amp;where=San-Diego__2c-CA" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL City Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="San Diego, CA">San Diego</a></li>
                                                <li onclick="triggerFilterClick(this, 'location')" class="showmoreCityLinks"><a href="https://www.monster.com/jobs/search/?q=Python&amp;where=San-Jose__2c-CA" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL City Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="San Jose, CA">San Jose</a></li>
                                                <li onclick="triggerFilterClick(this, 'location')" class="showmoreCityLinks"><a href="https://www.monster.com/jobs/search/?q=Python&amp;where=Austin__2c-TX" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL City Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Austin, TX">Austin</a></li>
                                                <li onclick="triggerFilterClick(this, 'location')" class="showmoreCityLinks"><a href="https://www.monster.com/jobs/search/?q=Python&amp;where=Sunnyvale__2c-CA" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL City Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Sunnyvale, CA">Sunnyvale</a></li>
                                                <li onclick="triggerFilterClick(this, 'location')" class="showmoreCityLinks"><a href="https://www.monster.com/jobs/search/?q=Python&amp;where=Palo-Alto__2c-CA" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL City Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Palo Alto, CA">Palo Alto</a></li>
                                        <li id="showlessCityButton" class="showlessButton">
                                            <a onclick="$('#showlessCityButton').hide();$('.showmoreCityLinks').hide();$('#showmoreCityButton').show();">Show Less <span class="mdi mdi-chevron-up"></span></a>
                                        </li>
                                </ul>
                            </li>
        </ul>
    </div>
    <br />
            <div class="refine similar-jobtitle">
                <div class="refine-section">
                    <h4>Related Job Titles:</h4>
                    <ul aria-label="Related Job Titles:">
                            <li onclick="triggerFilterClick(this, 'kywdjobtitle')">
                                <span class="label label-default refinement-tag">
                                    <span class="refinement-tag-text"><a href="https://www.monster.com/jobs/search/Software-Engineer_5" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Software Engineer">Software Engineer</a></span>
                                </span>
                            </li>
                            <li onclick="triggerFilterClick(this, 'kywdjobtitle')">
                                <span class="label label-default refinement-tag">
                                    <span class="refinement-tag-text"><a href="https://www.monster.com/jobs/search/Data-Scientist_5" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Data Scientist">Data Scientist</a></span>
                                </span>
                            </li>
                            <li onclick="triggerFilterClick(this, 'kywdjobtitle')">
                                <span class="label label-default refinement-tag">
                                    <span class="refinement-tag-text"><a href="https://www.monster.com/jobs/search/DevOps-Engineer_5" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="DevOps Engineer">DevOps Engineer</a></span>
                                </span>
                            </li>
                            <li onclick="triggerFilterClick(this, 'kywdjobtitle')">
                                <span class="label label-default refinement-tag">
                                    <span class="refinement-tag-text"><a href="https://www.monster.com/jobs/search/Quality-Assurance-Engineer_5" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Quality Assurance Engineer">Quality Assurance Engineer</a></span>
                                </span>
                            </li>
                            <li onclick="triggerFilterClick(this, 'kywdjobtitle')">
                                <span class="label label-default refinement-tag">
                                    <span class="refinement-tag-text"><a href="https://www.monster.com/jobs/search/Cloud-Computing-Engineer_5" onClick="dataLayer.push({&#39;eventCategory&#39;:&#39;Sidebar Widgets&#39;,&#39;eventAction&#39;:&#39;BL Title Short&#39;,&#39;eventLabel&#39;:&#39;Click Link in widget&#39;});" title="Cloud Computing Engineer">Cloud Computing Engineer</a></span>
                                </span>
                            </li>
                    </ul>
                </div>
            </div>
        <script type="text/javascript">
          //  $(document).ready(function () {
                $('.showmoreStateLinks').hide();
                $('.showmoreCityLinks').hide();
                $('.showmoreCompanyLinks').hide();
                $('.showmoreVerticalLinks').hide();
                $('.showmoreJobTitleLinks').hide();
                $('.showmoreSkillLinks').hide();
          //  });
        </script>


        </div>
        <div class="col-sm-8 col-lg-7 jsr-mid" xmlns:formatutils="urn:format-utils" xmlns:widgetmanager="urn:widget-manager" xmlns:contentblockmanager="urn:content-block-manager" xmlns:ms="urn:schemas-microsoft-com:xslt">
            <div class="row" id="main">
                <div class="col-xs-12 jsresultsheader">

    <div class="visible-xs" id="mobileEmailWidget">

<input type="hidden" id="searchQuery" value="q=Python&amp;brd=1&amp;brd=2&amp;cy=US&amp;pg=40&amp;pp=25&amp;sort=rv.di.dt&amp;stp=TwoBoxBand" />
<input type="hidden" id="isLoggedIn" value="false" />
<input type="hidden" id="maxSaveSearchesAllowed" value="5" />
<input type="hidden" id="emailUrl" value="https://www.monster.com/jobs/emailjobs?q=Python&amp;page=40" />
<input type="hidden" id="isDynamicPage" value="True" />

        <div class="jobAlertButton">
            <button type="submit" id="emailButton3" class="emailButton">Email me Jobs</button>
        </div>
      <div class="jobAlerts">

            <span class="jobAlert_Close" aria-label="Close" title="Close">X</span>
            <div class="marked-title clearfix">
                <h3><i class="fa fa-envelope"></i> Get jobs by email for this search</h3>
            </div>
            <div class="row">
                <div class="col-xs-12 col-sm-7 col-md-7">
                    <label class="sr-only" for="emailAddress">Enter Your Email Address</label>
                    <input type="text" placeholder="Enter Your Email Address" id="emailAddress1" name="emailAddress1" value="" class="form-control">
                </div>
                <div class="col-xs-12 col-sm-5 col-md-5">
                    <button data-loading-text="<i class='fa fa-spinner fa-spin'></i>" type="button" id="emailButton2" value="Email Me Jobs " title="Email me Jobs " onclick="dataLayer.push({'eventCategory':'Sidebar Widgets','eventAction':'JSA','eventLabel':'Click Link in Widget'});; emailActionMobileClick(this); ">
                        Email Me Jobs
                    </button>
                </div>
            </div>
            <div class="messageholder">
            </div>
            <div class="litRegPrivacy fnt1" runat="server" id="privacyMSG" visible="False">
                 By continuing you agree to Monster's <a title="privacy policy" target="_blank" href="http://my.monster.com/Privacy/Default.aspx">Privacy Policy</a>, <a title="terms of use" target="_blank" href="http://my.monster.com/Terms/Default.aspx">Terms of Use</a> and <a title="use of cookies" target="_blank" href="http://inside.monster.com/cookie-info/inside2.aspx">Use of Cookies</a>.
            </div>
         </div>



<script type="text/javascript">

    $(function() {
        setUpScroll();


        var isLoggedin = false;
        if (isLoggedin) {
            var emailAddr = getParameterByName('addr');
            var searchQuery =  $('#searchQuery').val();
            if (emailAddr && searchQuery) {
                dataLayer.push({'eventCategory':'Sidebar Widgets','eventAction':'JSA','eventLabel':'Click Link in Widget'});;
                emailAction(emailAddr, searchQuery);
             }
         }
    });

</script>




    </div>


<h1>
         Python Jobs - Page 40
</h1>



<h2 class="page-title hidden-xs">
    1000+ Jobs Found
</h2>
<h2 class="page-title visible-xs">
    1000+ Jobs Found
</h2>
                </div>


                <div class="col-xs-12">


<script type="application/ld+json">

            {"@context":"https://schema.org","@type":"ItemList","mainEntityOfPage":{
            "@type":"CollectionPage","@id":"https://www.monster.com/jobs/search/?q=Python&amp;page=40"
            }
            ,"itemListElement":[

                 {"@type":"ListItem","position":976,"url":"http://jobview.monster.com/software-engineer-c-job-natick-ma-us-182655058.aspx"}
                    ,
                 {"@type":"ListItem","position":977,"url":"http://jobview.monster.com/statistician-modeler-data-scientist-job-foster-city-ca-us-182662761.aspx"}
                    ,
                 {"@type":"ListItem","position":978,"url":"http://jobview.monster.com/bioinformatics-engineer-sequencing-2-job-santa-clara-ca-us-183114583.aspx"}
                    ,
                 {"@type":"ListItem","position":979,"url":"http://jobview.monster.com/applications-developer-job-new-york-ny-us-182646765.aspx"}
                    ,
                 {"@type":"ListItem","position":980,"url":"http://jobview.monster.com/ups-data-scientist-11809-4-11-17-job-wayne-nj-us-183127864.aspx"}
                    ,
                 {"@type":"ListItem","position":981,"url":"http://jobview.monster.com/etl-consultant-job-menlo-park-ca-us-182651519.aspx"}
                    ,
                 {"@type":"ListItem","position":982,"url":"http://jobview.monster.com/c-programmer-job-manhattan-ny-us-183193036.aspx"}
                    ,
                 {"@type":"ListItem","position":983,"url":"http://jobview.monster.com/service-management-tools-engineer-job-buffalo-ny-us-182662610.aspx"}
                    ,
                 {"@type":"ListItem","position":984,"url":"http://jobview.monster.com/software-design-engineer-in-test-job-seattle-wa-us-183193489.aspx"}
                    ,
                 {"@type":"ListItem","position":985,"url":"http://jobview.monster.com/sr-dev-ops-test-automation-engineer-job-berkeley-ca-us-183122453.aspx"}
                    ,
                 {"@type":"ListItem","position":986,"url":"http://jobview.monster.com/data-scientist-job-johnston-ia-us-183182405.aspx"}
                    ,
                 {"@type":"ListItem","position":987,"url":"http://jobview.monster.com/software-engineer-job-bellevue-wa-us-183202077.aspx"}
                    ,
                 {"@type":"ListItem","position":988,"url":"http://jobview.monster.com/senior-mobile-engineer-%e2%80%93-ios-technical-architect-7326-job-auburn-hills-mi-us-183264371.aspx"}
                    ,
                 {"@type":"ListItem","position":989,"url":"http://jobview.monster.com/systems-administrator-job-minneapolis-mn-us-183193343.aspx"}
                    ,
                 {"@type":"ListItem","position":990,"url":"http://jobview.monster.com/application-support-engineer-investment-firm-w-sql-job-new-york-ny-us-182664270.aspx"}
                    ,
                 {"@type":"ListItem","position":991,"url":"http://jobview.monster.com/hardware-design-engineer-job-fremont-ca-us-183073519.aspx"}
                    ,
                 {"@type":"ListItem","position":992,"url":"http://jobview.monster.com/technical-writer-job-new-york-ny-us-183080095.aspx"}
                    ,
                 {"@type":"ListItem","position":993,"url":"http://jobview.monster.com/jr-software-engineer-job-burlington-ma-us-183070536.aspx"}
                    ,
                 {"@type":"ListItem","position":994,"url":"http://jobview.monster.com/lamp-software-engineer-job-atlanta-ga-us-183080083.aspx"}
                    ,
                 {"@type":"ListItem","position":995,"url":"http://jobview.monster.com/software-engineer-virtualization-job-boston-ma-us-182651205.aspx"}
                    ,
                 {"@type":"ListItem","position":996,"url":"http://jobview.monster.com/senior-ios-developer-job-salt-lake-city-ut-us-182638389.aspx"}
                    ,
                 {"@type":"ListItem","position":997,"url":"http://jobview.monster.com/sql-database-developer-job-boston-ma-us-182652886.aspx"}
                    ,
                 {"@type":"ListItem","position":998,"url":"http://jobview.monster.com/senior-software-engineer-encirca-job-johnston-ia-us-183182189.aspx"}
                    ,
                 {"@type":"ListItem","position":999,"url":"http://jobview.monster.com/data-scientist-job-boston-ma-us-182655103.aspx"}
                    ,
                 {"@type":"ListItem","position":1000,"url":"http://jobview.monster.com/hitl-software-engineer-job-wright-patterson-afb-oh-us-182543385.aspx"}
            ]}


</script>
    <section id="resultsWrapper">
                    <div class="js_result_container featured-ad clearfix">
                        <script language="javaScript" type="text/javascript" id="AdScript_Middle_FeaturedEmployer" name="AdScript_Middle_FeaturedEmployer">
	var OAS_RNS = 879145638;
                                                        var OAS_taxonomy='site=mons&affiliate=mons&app=js&size=0x112&oas_pv=no_analytics&key=python&fb=0&dx=1160001&dx=1188600&dx=mon&dx=2291224&dx=2291290&dx=2291224&cy=US&plid=20586&pcid=660&poccid=11970&sapp=jsr&app=js';
                                                        var OAS_query='site=mons&affiliate=mons&app=js&size=0x112&oas_pv=no_analytics&key=python&fb=0&dx=1160001&dx=1188600&dx=mon&dx=2291224&dx=2291290&dx=2291224&cy=US&plid=20586&pcid=660&poccid=11970&sapp=jsr&app=js';
	                                                    OAS_query == '' ? OAS_query+='XE' + '&' + OAS_taxonomy + OAS_rdl + "&if_nt_CookieAccept=" + OAS_CA + '&XE': OAS_query+= '&XE' + '&' + OAS_taxonomy + OAS_rdl + "&if_nt_CookieAccept=" + OAS_CA + '&XE';
	                                                    document.write('<iframe width=100% height=112 id=AdFrame_Middle_FeaturedEmployer name=AdFrame_Middle_FeaturedEmployer class="" marginwidth=0 marginheight=0 hspace=0 vspace=0 frameborder=0 scrolling=no bordercolor="#000000" src="https://oas.monster.com/RealMedia/ads/adstream_sx.ads/us.monster.en/jsrnew/powersearch.aspx/1' + OAS_RNS + '@Middle,BottomRight,Left1,Left2,Middle1,Left3,Right3,Right,Right1,Right2,x42,x18,Bottom1,Top,TopRight!Middle?' + OAS_query + '" title="Advertisement"></iframe>');

</script>
                    </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xsworld1x" data-m_impr_j_jawsid="228311313" data-m_impr_j_jobid="182655058" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="42.2834" data-m_impr_j_lid="453" data-m_impr_j_long="-71.3495" data-m_impr_j_occid="11904" data-m_impr_j_p="1" data-m_impr_j_postingid="86b66f19-41bb-4a74-8766-9d5d50debb30" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="78668435-f2df-46f7-a1b3-a887baf597c4" href="http://jobview.monster.com/software-engineer-c-job-natick-ma-us-182655058.aspx?mescoid=1500127001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;1&#39;});; clickJobTitle(&#39;plid=453&amp;pcid=660&amp;poccid=11904&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Software Engineer - C++&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xsworld1x_Softworld Inc&quot;,&quot;eVar31&quot;:&quot;Natick_MA_&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-19T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Software Engineer - C++"><span itemprop="title">Software Engineer - C++</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-softworld-inc.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;1&#39;});" rel="nofollow" title="Softworld Inc"><span itemprop="name">Softworld Inc</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-natick,-ma.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;1&#39;});" title="Natick, MA"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Natick, MA
            <meta itemprop="addressLocality" content="Natick" />
            <meta itemprop="addressRegion" content="MA" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-19T12:00" itemprop="datePosted">3 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Software Engineer
Framingham, MA

Description:
The position requires a Software Engineer for consumer product development with audio applications.
Design and develop embedded network applications on Linux platform in a Scrum/Agile environment.
Own p......" />
                    <meta itemprop="url" content="http://jobview.monster.com/software-engineer-c-job-natick-ma-us-182655058.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xwebxlx" data-m_impr_j_jawsid="228331084" data-m_impr_j_jobid="182662761" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="37.5585" data-m_impr_j_lid="883" data-m_impr_j_long="-122.2711" data-m_impr_j_occid="11904" data-m_impr_j_p="2" data-m_impr_j_postingid="83fd78bf-3933-4d9b-a534-a39375310b5f" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="8ace4667-da75-4bd7-a837-e0fd95408def" href="http://jobview.monster.com/statistician-modeler-data-scientist-job-foster-city-ca-us-182662761.aspx?mescoid=1500142001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;2&#39;});; clickJobTitle(&#39;plid=883&amp;pcid=660&amp;poccid=11904&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Statistician / Modeler / Data Scientist&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xwebxlx_Collabera&quot;,&quot;eVar31&quot;:&quot;Foster City_CA_&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-19T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Statistician / Modeler / Data Scientist"><span itemprop="title">Statistician / Modeler / Data Scientist</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-collabera.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;2&#39;});" rel="nofollow" title="Collabera"><span itemprop="name">Collabera</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-foster-city,-ca.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;2&#39;});" title="Foster City, CA"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Foster City, CA
            <meta itemprop="addressLocality" content="Foster City" />
            <meta itemprop="addressRegion" content="CA" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-19T12:00" itemprop="datePosted">3 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Position Details:
Job Title:  Statistician/Modeler
Duration:  6 months, Contract to Hire
Location:  Highlands Ranch, CO   Foster City, CA
Interview:   Phone &amp; Onsite

Description:
Responsible for developing statistical predictive models using Operat......" />
                    <meta itemprop="url" content="http://jobview.monster.com/statistician-modeler-data-scientist-job-foster-city-ca-us-182662761.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="559" data-m_impr_j_coc="xw96967341wx" data-m_impr_j_jawsid="230676361" data-m_impr_j_jobid="183114583" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="37.3519" data-m_impr_j_lid="356" data-m_impr_j_long="-121.952" data-m_impr_j_occid="11921" data-m_impr_j_p="3" data-m_impr_j_postingid="38cea8b2-8554-4849-b6cb-b05f93116dde" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="41251746-9888-4536-86dc-639bd3c9670d" href="http://jobview.monster.com/bioinformatics-engineer-sequencing-2-job-santa-clara-ca-us-183114583.aspx?mescoid=1900245001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;3&#39;});; clickJobTitle(&#39;plid=356&amp;pcid=559&amp;poccid=11921&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Bioinformatics Engineer - Sequencing (2)&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xw96967341wx_HLM Staffing Solutions&quot;,&quot;eVar31&quot;:&quot;Santa Clara_CA_95050&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-18T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Bioinformatics Engineer - Sequencing (2)"><span itemprop="title">Bioinformatics Engineer - Sequencing (2)</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-hlm-staffing-solutions.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;3&#39;});" rel="nofollow" title="HLM Staffing Solutions"><span itemprop="name">HLM Staffing Solutions</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-santa-clara,-ca.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;3&#39;});" title="Santa Clara, CA, 95050"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Santa Clara, CA
            <meta itemprop="addressLocality" content="Santa Clara" />
            <meta itemprop="addressRegion" content="CA" />
            <meta itemprop="postalCode" content="95050" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-18T12:00" itemprop="datePosted">4 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="The data science group here is not like those at other companies. We generate and process massive amounts of sequencing data on a system designed and built in-house from the ground up. As a Bioinformatics Data Scientist at Roche Sequencing Santa Cla......" />
                    <meta itemprop="url" content="http://jobview.monster.com/bioinformatics-engineer-sequencing-2-job-santa-clara-ca-us-183114583.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xkforcex" data-m_impr_j_jawsid="228293111" data-m_impr_j_jobid="182646765" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="40.7546" data-m_impr_j_lid="550" data-m_impr_j_long="-73.9736" data-m_impr_j_occid="11772" data-m_impr_j_p="4" data-m_impr_j_postingid="7b07ab41-0199-45c9-9c87-448058d57c44" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="bf84350d-37d8-4bdf-a70c-e9996a05d25a" href="http://jobview.monster.com/applications-developer-job-new-york-ny-us-182646765.aspx?mescoid=1500127001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;4&#39;});; clickJobTitle(&#39;plid=550&amp;pcid=660&amp;poccid=11772&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Applications Developer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xkforcex_Kforce Inc&quot;,&quot;eVar31&quot;:&quot;New York_NY_10172&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-19T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Applications Developer"><span itemprop="title">Applications Developer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-kforce-professional-staffing.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;4&#39;});" title="Kforce Inc"><span itemprop="name">Kforce Inc</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-new-york-city,-ny.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;4&#39;});" title="New York, NY, 10172"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    New York, NY
            <meta itemprop="addressLocality" content="New York" />
            <meta itemprop="addressRegion" content="NY" />
            <meta itemprop="postalCode" content="10172" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-19T12:00" itemprop="datePosted">3 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="RESPONSIBILITIES:A Kforce client is seeking an Applications Developer in New York, NY.   Designs, analyzes, develops, codes, tests, debugs and documents programming to satisfy business requirements. Proficient in application development skills for m......" />
                    <meta itemprop="url" content="http://jobview.monster.com/applications-developer-job-new-york-ny-us-182646765.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary has-bolding">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xupswrapx" data-m_impr_j_jawsid="230729178" data-m_impr_j_jobid="183127864" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="40.9484" data-m_impr_j_lid="534" data-m_impr_j_long="-74.2449" data-m_impr_j_occid="11904" data-m_impr_j_p="5" data-m_impr_j_postingid="2cbb3253-384c-4afb-b281-40682d32bf0d" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="ecce794e-7757-4fcb-a1c6-b216105604dc" href="http://jobview.monster.com/ups-data-scientist-11809-4-11-17-job-wayne-nj-us-183127864.aspx?mescoid=1500152001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;5&#39;});; clickJobTitle(&#39;plid=534&amp;pcid=660&amp;poccid=11904&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;UPS Data Scientist- 11809 4/11/17&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xupswrapx_UPS&quot;,&quot;eVar31&quot;:&quot;Wayne_NJ_07470&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-18T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="UPS Data Scientist- 11809 4/11/17"><span itemprop="title">UPS Data Scientist- 11809 4/11/17</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-ups.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;5&#39;});" rel="nofollow" title="UPS"><span itemprop="name">UPS</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-wayne,-nj.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;5&#39;});" title="Wayne, NJ, 07470"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Wayne, NJ
            <meta itemprop="addressLocality" content="Wayne" />
            <meta itemprop="addressRegion" content="NJ" />
            <meta itemprop="postalCode" content="07470" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-18T12:00" itemprop="datePosted">4 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Data Scientist

Internal Job Title: Intermediate Applications Developer

We’re the obstacle overcomers, the problem get-arounders. From figuring it out to getting it done... our innovative culture demands “yes and how!” We are UPS.  We are the Unite......" />
                    <meta itemprop="url" content="http://jobview.monster.com/ups-data-scientist-11809-4-11-17-job-wayne-nj-us-183127864.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xwebxlx" data-m_impr_j_jawsid="228303992" data-m_impr_j_jobid="182651519" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="37.4538" data-m_impr_j_lid="883" data-m_impr_j_long="-122.1822" data-m_impr_j_occid="11904" data-m_impr_j_p="6" data-m_impr_j_postingid="7a5f8f2b-4774-48e7-bddd-5404013a6e5f" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="ffb8b50c-28e4-447a-a80d-7bc9409240b1" href="http://jobview.monster.com/etl-consultant-job-menlo-park-ca-us-182651519.aspx?mescoid=1500143001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;6&#39;});; clickJobTitle(&#39;plid=883&amp;pcid=660&amp;poccid=11904&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;ETL Consultant&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xwebxlx_Collabera&quot;,&quot;eVar31&quot;:&quot;Menlo Park_CA_&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-19T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="ETL Consultant"><span itemprop="title">ETL Consultant</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-collabera.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;6&#39;});" rel="nofollow" title="Collabera"><span itemprop="name">Collabera</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-menlo-park,-ca.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;6&#39;});" title="Menlo Park, CA"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Menlo Park, CA
            <meta itemprop="addressLocality" content="Menlo Park" />
            <meta itemprop="addressRegion" content="CA" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-19T12:00" itemprop="datePosted">3 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Job Responsibilities
Other capabilities should include:
• Experience in Agile delivery
• Fast learner/adaptive
For the Ingestion components
• AWS experience
• Python
• Shell/unix/scripting languages
• Familiar with Big Data integration – Hadoop, hiv......" />
                    <meta itemprop="url" content="http://jobview.monster.com/etl-consultant-job-menlo-park-ca-us-182651519.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xrmscorpx" data-m_impr_j_jawsid="230958159" data-m_impr_j_jobid="183193036" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="40.7201" data-m_impr_j_lid="550" data-m_impr_j_long="-74.0047" data-m_impr_j_occid="11904" data-m_impr_j_p="7" data-m_impr_j_postingid="772f5c34-ddd0-4b8c-896f-128f1cd29080" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="ce6e702b-c131-428d-ade0-4523610989f8" href="http://jobview.monster.com/c-programmer-job-manhattan-ny-us-183193036.aspx?mescoid=1500127001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;7&#39;});; clickJobTitle(&#39;plid=550&amp;pcid=660&amp;poccid=11904&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;C++ Programmer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xrmscorpx_RMS Computer Corporation&quot;,&quot;eVar31&quot;:&quot;Manhattan_NY_10013&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-19T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="C++ Programmer"><span itemprop="title">C++ Programmer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-rms-computer-corporation.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;7&#39;});" title="RMS Computer Corporation"><span itemprop="name">RMS Computer Corporation</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-manhattan,-ny.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;7&#39;});" title="Manhattan, NY, 10013"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Manhattan, NY
            <meta itemprop="addressLocality" content="Manhattan" />
            <meta itemprop="addressRegion" content="NY" />
            <meta itemprop="postalCode" content="10013" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-19T12:00" itemprop="datePosted">3 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Our client, a leading global financial services company, has approximately 200 million customer accounts and does business in more than 140 countries. They provide consumers, corporations, governments and institutions with financial products and ser......" />
                    <meta itemprop="url" content="http://jobview.monster.com/c-programmer-job-manhattan-ny-us-183193036.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xwebxlx" data-m_impr_j_jawsid="228330997" data-m_impr_j_jobid="182662610" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="42.8864" data-m_impr_j_lid="546" data-m_impr_j_long="-78.8784" data-m_impr_j_occid="11904" data-m_impr_j_p="8" data-m_impr_j_postingid="70a3fdc2-6462-4f60-9118-5563db351cff" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="0a65d2c2-bb22-49f8-966a-5cf1020abc49" href="http://jobview.monster.com/service-management-tools-engineer-job-buffalo-ny-us-182662610.aspx?mescoid=1700178001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;8&#39;});; clickJobTitle(&#39;plid=546&amp;pcid=660&amp;poccid=11904&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Service Management Tools Engineer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xwebxlx_Collabera&quot;,&quot;eVar31&quot;:&quot;Buffalo_NY_&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-19T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Service Management Tools Engineer"><span itemprop="title">Service Management Tools Engineer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-collabera.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;8&#39;});" rel="nofollow" title="Collabera"><span itemprop="name">Collabera</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-buffalo,-ny.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;8&#39;});" title="Buffalo, NY"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Buffalo, NY
            <meta itemprop="addressLocality" content="Buffalo" />
            <meta itemprop="addressRegion" content="NY" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-19T12:00" itemprop="datePosted">3 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Description:
The Tooling CoE implementation engineer is charged with executing implementation and deployment activities for the tools within the CoE service catalog.
This includes tools such as AppDynamics,  Dynatrace, Splunk &amp; ELK, and others.
......" />
                    <meta itemprop="url" content="http://jobview.monster.com/service-management-tools-engineer-job-buffalo-ny-us-182662610.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xmotivwax" data-m_impr_j_jawsid="230958293" data-m_impr_j_jobid="183193489" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="47.6157" data-m_impr_j_lid="647" data-m_impr_j_long="-122.3445" data-m_impr_j_occid="11970" data-m_impr_j_p="9" data-m_impr_j_postingid="682b7739-3d72-424f-8897-f6dd32c79845" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="02594cf2-83ca-40a4-a863-b57ec4fdf12c" href="http://jobview.monster.com/software-design-engineer-in-test-job-seattle-wa-us-183193489.aspx?mescoid=1500137001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;9&#39;});; clickJobTitle(&#39;plid=647&amp;pcid=660&amp;poccid=11970&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Software Design Engineer in Test&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xmotivwax_Motiv, Inc.&quot;,&quot;eVar31&quot;:&quot;Seattle_WA_98121&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-19T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Software Design Engineer in Test"><span itemprop="title">Software Design Engineer in Test</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-motiv__2c-inc__2e.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;9&#39;});" rel="nofollow" title="Motiv, Inc."><span itemprop="name">Motiv, Inc.</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-seattle,-wa.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;9&#39;});" title="Seattle, WA, 98121"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Seattle, WA
            <meta itemprop="addressLocality" content="Seattle" />
            <meta itemprop="addressRegion" content="WA" />
            <meta itemprop="postalCode" content="98121" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-19T12:00" itemprop="datePosted">3 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="We are looking for an outstanding SDET to join our team and assist our client in the Greater Seattle Area. Our SDET’s are eligible to work for wonderful organizations in the area that offer cloud-based services and create effortless and innovative e......" />
                    <meta itemprop="url" content="http://jobview.monster.com/software-design-engineer-in-test-job-seattle-wa-us-183193489.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xredfishtecx" data-m_impr_j_jawsid="230699853" data-m_impr_j_jobid="183122453" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="37.865" data-m_impr_j_lid="702" data-m_impr_j_long="-122.2386" data-m_impr_j_occid="11970" data-m_impr_j_p="10" data-m_impr_j_postingid="0e9045a1-afc0-4208-8ac5-aa65c4540996" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="cb3bb45a-e366-4eee-b4bb-d5a585827a01" href="http://jobview.monster.com/sr-dev-ops-test-automation-engineer-job-berkeley-ca-us-183122453.aspx?mescoid=1500137001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;10&#39;});; clickJobTitle(&#39;plid=702&amp;pcid=660&amp;poccid=11970&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Sr Dev/Ops/Test Automation Engineer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xredfishtecx_Redfish Technology&quot;,&quot;eVar31&quot;:&quot;Berkeley_CA_94705&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-18T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Sr Dev/Ops/Test Automation Engineer"><span itemprop="title">Sr Dev/Ops/Test Automation Engineer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-redfish-technology.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;10&#39;});" title="Redfish Technology"><span itemprop="name">Redfish Technology</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-berkeley,-ca.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;10&#39;});" title="Berkeley, CA, 94705"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Berkeley, CA
            <meta itemprop="addressLocality" content="Berkeley" />
            <meta itemprop="addressRegion" content="CA" />
            <meta itemprop="postalCode" content="94705" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-18T12:00" itemprop="datePosted">4 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Your  Role


You will be  collaborating closely with our VP of Engineering to build and extend the   infrastructure for development, testing, and deployment. Our customers are  strictly regulated entities in industries such as financial services and......" />
                    <meta itemprop="url" content="http://jobview.monster.com/sr-dev-ops-test-automation-engineer-job-berkeley-ca-us-183122453.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="559" data-m_impr_j_coc="xgen10x" data-m_impr_j_jawsid="230935271" data-m_impr_j_jobid="183182405" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="41.689" data-m_impr_j_lid="406" data-m_impr_j_long="-93.7182" data-m_impr_j_occid="11912" data-m_impr_j_p="11" data-m_impr_j_postingid="6472c7c9-18dd-4b7c-a758-ee600b5be108" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="47774127-d513-46b9-9d96-f17328f75897" href="http://jobview.monster.com/data-scientist-job-johnston-ia-us-183182405.aspx?mescoid=1500152001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;11&#39;});; clickJobTitle(&#39;plid=406&amp;pcid=559&amp;poccid=11912&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Data Scientist&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xgen10x_Genesis10&quot;,&quot;eVar31&quot;:&quot;Johnston_IA_50131&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-19T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Data Scientist"><span itemprop="title">Data Scientist</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-genesis10.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;11&#39;});" title="Genesis10"><span itemprop="name">Genesis10</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-johnston,-ia.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;11&#39;});" title="Johnston, IA, 50131"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Johnston, IA
            <meta itemprop="addressLocality" content="Johnston" />
            <meta itemprop="addressRegion" content="IA" />
            <meta itemprop="postalCode" content="50131" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-19T12:00" itemprop="datePosted">3 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="No third parties please.  We are unable to sponsor H1 visas at this time.  All candidates MUST be able to attend an IN PERSON interview.

Genesis10 is actively seeking Data Scientist for a Direct Hire positon with our client located in Des Moines, ......" />
                    <meta itemprop="url" content="http://jobview.monster.com/data-scientist-job-johnston-ia-us-183182405.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
                    <div class="js_result_container featured-ad clearfix">
                        <script language="javaScript" type="text/javascript" id="AdScript_Left1_FeaturedJob" name="AdScript_Left1_FeaturedJob">
	var OAS_RNS = 879145638;
                                                        var OAS_taxonomy='site=mons&affiliate=mons&app=js&size=0x101&oas_pv=no_analytics&key=python&fb=0&dx=1160001&dx=1188600&dx=mon&dx=2291224&dx=2291290&dx=2291224&cy=US&plid=20586&pcid=660&poccid=11970&sapp=jsr&app=js';
                                                        var OAS_query='site=mons&affiliate=mons&app=js&size=0x101&oas_pv=no_analytics&key=python&fb=0&dx=1160001&dx=1188600&dx=mon&dx=2291224&dx=2291290&dx=2291224&cy=US&plid=20586&pcid=660&poccid=11970&sapp=jsr&app=js';
	                                                    OAS_query == '' ? OAS_query+='XE' + '&' + OAS_taxonomy + OAS_rdl + "&if_nt_CookieAccept=" + OAS_CA + '&XE': OAS_query+= '&XE' + '&' + OAS_taxonomy + OAS_rdl + "&if_nt_CookieAccept=" + OAS_CA + '&XE';
	                                                    document.write('<iframe width=100% height=101 id=AdFrame_Left1_FeaturedJob name=AdFrame_Left1_FeaturedJob class="" marginwidth=0 marginheight=0 hspace=0 vspace=0 frameborder=0 scrolling=no bordercolor="#000000" src="https://oas.monster.com/RealMedia/ads/adstream_sx.ads/us.monster.en/jsrnew/powersearch.aspx/1' + OAS_RNS + '@Middle,BottomRight,Left1,Left2,Middle1,Left3,Right3,Right,Right1,Right2,x42,x18,Bottom1,Top,TopRight!Left1?' + OAS_query + '" title="Advertisement"></iframe>');

</script>
                    </div>
                    <div class="js_result_container featured-ad clearfix">
                        <script language="javaScript" type="text/javascript" id="AdScript_Left2_FeaturedOpportunity" name="AdScript_Left2_FeaturedOpportunity">
	var OAS_RNS = 879145638;
                                                        var OAS_taxonomy='site=mons&affiliate=mons&app=js&size=0x101&oas_pv=no_analytics&key=python&fb=0&dx=1160001&dx=1188600&dx=mon&dx=2291224&dx=2291290&dx=2291224&cy=US&plid=20586&pcid=660&poccid=11970&sapp=jsr&app=js';
                                                        var OAS_query='site=mons&affiliate=mons&app=js&size=0x101&oas_pv=no_analytics&key=python&fb=0&dx=1160001&dx=1188600&dx=mon&dx=2291224&dx=2291290&dx=2291224&cy=US&plid=20586&pcid=660&poccid=11970&sapp=jsr&app=js';
	                                                    OAS_query == '' ? OAS_query+='XE' + '&' + OAS_taxonomy + OAS_rdl + "&if_nt_CookieAccept=" + OAS_CA + '&XE': OAS_query+= '&XE' + '&' + OAS_taxonomy + OAS_rdl + "&if_nt_CookieAccept=" + OAS_CA + '&XE';
	                                                    document.write('<iframe width=100% height=101 id=AdFrame_Left2_FeaturedOpportunity name=AdFrame_Left2_FeaturedOpportunity class="" marginwidth=0 marginheight=0 hspace=0 vspace=0 frameborder=0 scrolling=no bordercolor="#000000" src="https://oas.monster.com/RealMedia/ads/adstream_sx.ads/us.monster.en/jsrnew/powersearch.aspx/1' + OAS_RNS + '@Middle,BottomRight,Left1,Left2,Middle1,Left3,Right3,Right,Right1,Right2,x42,x18,Bottom1,Top,TopRight!Left2?' + OAS_query + '" title="Advertisement"></iframe>');

</script>
                    </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="" data-m_impr_j_jawsid="230989469" data-m_impr_j_jobid="183202077" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="47.6186" data-m_impr_j_lid="896" data-m_impr_j_long="-122.204" data-m_impr_j_occid="11904" data-m_impr_j_p="12" data-m_impr_j_postingid="5fe662d0-4b07-4bee-9f0d-829a869eac8c" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="6561ce86-43cc-4622-8a09-dcf78a2f9764" href="http://jobview.monster.com/software-engineer-job-bellevue-wa-us-183202077.aspx?mescoid=1500127001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;12&#39;});; clickJobTitle(&#39;plid=896&amp;pcid=660&amp;poccid=11904&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Software Engineer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;_Company Confidential&quot;,&quot;eVar31&quot;:&quot;Bellevue_WA_98004&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-19T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Software Engineer"><span itemprop="title">Software Engineer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
                                <span itemprop="name">Company Confidential</span>
                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-bellevue,-wa.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;12&#39;});" title="Bellevue, WA, 98004"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Bellevue, WA
            <meta itemprop="addressLocality" content="Bellevue" />
            <meta itemprop="addressRegion" content="WA" />
            <meta itemprop="postalCode" content="98004" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-19T12:00" itemprop="datePosted">3 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Looking for strong developers in Java, Go, Scala or Python
Big data experience is a big plus but not a must
3+ years related work experience
Bachelor degree in Computer science or related field
Send me your resumes if you are interested..." />
                    <meta itemprop="url" content="http://jobview.monster.com/software-engineer-job-bellevue-wa-us-183202077.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xvshyderabadx" data-m_impr_j_jawsid="231335226" data-m_impr_j_jobid="183264371" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="42.6398" data-m_impr_j_lid="470" data-m_impr_j_long="-83.2944" data-m_impr_j_occid="11904" data-m_impr_j_p="13" data-m_impr_j_postingid="fd8d37d3-2411-4b23-b6b9-55a80d57f732" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="eac85c51-5841-4d15-91c0-200ab26f9733" href="http://jobview.monster.com/senior-mobile-engineer-%E2%80%93-ios-technical-architect-7326-job-auburn-hills-mi-us-183264371.aspx?mescoid=1500138001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;13&#39;});; clickJobTitle(&#39;plid=470&amp;pcid=660&amp;poccid=11904&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Senior Mobile Engineer – iOS (Technical Architect)- 7326&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xvshyderabadx_V-Soft Consulting Group, Inc.&quot;,&quot;eVar31&quot;:&quot;Auburn Hills_MI_48321&quot;,&quot;prop24&quot;:&quot;2017-04-17T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Senior Mobile Engineer – iOS (Technical Architect)- 7326"><span itemprop="title">Senior Mobile Engineer – iOS (Technical Architect)- 7326</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-v__2dsoft-consulting-group__2c-inc__2e.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;13&#39;});" rel="nofollow" title="V-Soft Consulting Group, Inc."><span itemprop="name">V-Soft Consulting Group, Inc.</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-auburn-hills,-mi.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;13&#39;});" title="Auburn Hills, MI, 48321"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Auburn Hills, MI
            <meta itemprop="addressLocality" content="Auburn Hills" />
            <meta itemprop="addressRegion" content="MI" />
            <meta itemprop="postalCode" content="48321" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-17T12:00" itemprop="datePosted">5 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Senior Mobile Engineer – iOS (Technical Architect)

Primary Location – Auburn Hills, MI

Contractual Opportunities

V-Soft Consulting is currently hiring for a Senior Mobile Engineer – iOS (Technical Architect) our premier client in Auburn Hills, ......" />
                    <meta itemprop="url" content="http://jobview.monster.com/senior-mobile-engineer-%e2%80%93-ios-technical-architect-7326-job-auburn-hills-mi-us-183264371.aspx" />
                    <meta itemprop="employmentType" content="" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xkforcex" data-m_impr_j_jawsid="230958167" data-m_impr_j_jobid="183193343" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="44.9758" data-m_impr_j_lid="483" data-m_impr_j_long="-93.2715" data-m_impr_j_occid="11882" data-m_impr_j_p="14" data-m_impr_j_postingid="5c177f55-eeb7-477b-8f84-2a067c196bbc" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="685d0340-14f2-42f2-a388-01dca0002414" href="http://jobview.monster.com/systems-administrator-job-minneapolis-mn-us-183193343.aspx?mescoid=1500131001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;14&#39;});; clickJobTitle(&#39;plid=483&amp;pcid=660&amp;poccid=11882&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Systems Administrator&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xkforcex_Kforce Inc&quot;,&quot;eVar31&quot;:&quot;Minneapolis_MN_55402&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-19T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Systems Administrator"><span itemprop="title">Systems Administrator</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-kforce-professional-staffing.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;14&#39;});" title="Kforce Inc"><span itemprop="name">Kforce Inc</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-minneapolis,-mn.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;14&#39;});" title="Minneapolis, MN, 55402"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Minneapolis, MN
            <meta itemprop="addressLocality" content="Minneapolis" />
            <meta itemprop="addressRegion" content="MN" />
            <meta itemprop="postalCode" content="55402" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-19T12:00" itemprop="datePosted">3 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="RESPONSIBILITIES:Kforce has a client seeking a Systems Administrator 3 in Minneapolis, MN.    Essential Functions:
-  Provide advice and recommendations to management to assist in technology decisions &amp; direction
-  Perform research and analysis......" />
                    <meta itemprop="url" content="http://jobview.monster.com/systems-administrator-job-minneapolis-mn-us-183193343.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xkforcex" data-m_impr_j_jawsid="228337187" data-m_impr_j_jobid="182664270" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="40.7495" data-m_impr_j_lid="550" data-m_impr_j_long="-73.9791" data-m_impr_j_occid="11969" data-m_impr_j_p="15" data-m_impr_j_postingid="59da03c8-324e-4bbb-8614-272974d325cf" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="78acd5ea-30c4-4543-bf3e-56de82874916" href="http://jobview.monster.com/application-support-engineer-investment-firm-w-sql-job-new-york-ny-us-182664270.aspx?mescoid=1500134001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;15&#39;});; clickJobTitle(&#39;plid=550&amp;pcid=660&amp;poccid=11969&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Application Support Engineer-Investment Firm w/SQL&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xkforcex_Kforce Inc&quot;,&quot;eVar31&quot;:&quot;New York_NY_10154&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-19T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Application Support Engineer-Investment Firm w/SQL"><span itemprop="title">Application Support Engineer-Investment Firm w/SQL</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-kforce-professional-staffing.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;15&#39;});" title="Kforce Inc"><span itemprop="name">Kforce Inc</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-new-york-city,-ny.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;15&#39;});" title="New York, NY, 10154"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    New York, NY
            <meta itemprop="addressLocality" content="New York" />
            <meta itemprop="addressRegion" content="NY" />
            <meta itemprop="postalCode" content="10154" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-19T12:00" itemprop="datePosted">3 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="RESPONSIBILITIES:Kforce is working with a well-known investment firm located in New York, New York (NY) that is seeking an Application Support Engineer.  Summary: As a member of the Innovations and Infrastructure Team at this firm, the candidate wil......" />
                    <meta itemprop="url" content="http://jobview.monster.com/application-support-engineer-investment-firm-w-sql-job-new-york-ny-us-182664270.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="4" data-m_impr_j_coc="x500568hjsx" data-m_impr_j_jawsid="230531093" data-m_impr_j_jobid="183073519" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="37.4993" data-m_impr_j_lid="702" data-m_impr_j_long="-121.9787" data-m_impr_j_occid="11782" data-m_impr_j_p="16" data-m_impr_j_postingid="ec7c135a-8533-4b1a-9abd-40561b90f569" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="45bea0aa-9d5e-4d93-be22-85db8f2b6e21" href="http://jobview.monster.com/hardware-design-engineer-job-fremont-ca-us-183073519.aspx?mescoid=1700168001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;16&#39;});; clickJobTitle(&#39;plid=702&amp;pcid=4&amp;poccid=11782&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Hardware Design Engineer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;x500568hjsx_Themis Computer&quot;,&quot;eVar31&quot;:&quot;Fremont_CA_94538&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-17T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Hardware Design Engineer"><span itemprop="title">Hardware Design Engineer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-themis-computer.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;16&#39;});" rel="nofollow" title="Themis Computer"><span itemprop="name">Themis Computer</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-fremont,-ca.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;16&#39;});" title="Fremont, CA, 94538"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Fremont, CA
            <meta itemprop="addressLocality" content="Fremont" />
            <meta itemprop="addressRegion" content="CA" />
            <meta itemprop="postalCode" content="94538" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-17T12:00" itemprop="datePosted">5 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Hardware Engineer



Themis Computer is seeking multiple Hardware Engineers to work in a team on leading edge digital computer board designs. Successful candidates will have the opportunity to work on a diverse range of products, from rugged credit......" />
                    <meta itemprop="url" content="http://jobview.monster.com/hardware-design-engineer-job-fremont-ca-us-183073519.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xsolomon1x" data-m_impr_j_jawsid="230547269" data-m_impr_j_jobid="183080095" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="40.7409" data-m_impr_j_lid="550" data-m_impr_j_long="-73.9997" data-m_impr_j_occid="11904" data-m_impr_j_p="17" data-m_impr_j_postingid="ec529910-b333-407d-9ca8-7a2838e13eb9" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="82a91535-f7ea-48a5-af14-9d8a56ae96d1" href="http://jobview.monster.com/technical-writer-job-new-york-ny-us-183080095.aspx?mescoid=2700440001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;17&#39;});; clickJobTitle(&#39;plid=550&amp;pcid=660&amp;poccid=11904&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Technical Writer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xsolomon1x_Solomon Page&quot;,&quot;eVar31&quot;:&quot;New York_NY_10011&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-17T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Technical Writer"><span itemprop="title">Technical Writer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-solomon-page-group%2c-llc.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;17&#39;});" title="Solomon Page"><span itemprop="name">Solomon Page</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-new-york-city,-ny.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;17&#39;});" title="New York, NY, 10011"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    New York, NY
            <meta itemprop="addressLocality" content="New York" />
            <meta itemprop="addressRegion" content="NY" />
            <meta itemprop="postalCode" content="10011" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-17T12:00" itemprop="datePosted">5 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Most Days You:
- Contribute to documentation for developers about new technologies and tools
- Determine which digital features need to be documented
- Manage developer guide with API&#39;s
- Fix errors reported by users
- Work with SME to create docume......" />
                    <meta itemprop="url" content="http://jobview.monster.com/technical-writer-job-new-york-ny-us-183080095.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xworkableukx" data-m_impr_j_jawsid="230528643" data-m_impr_j_jobid="183070536" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="42.5048" data-m_impr_j_lid="893" data-m_impr_j_long="-71.1957" data-m_impr_j_occid="11904" data-m_impr_j_p="18" data-m_impr_j_postingid="e845a0be-3628-484a-95cb-b22dfa6deb74" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="4584579f-9cf6-4fe6-ab49-0b5db90b0f2c" href="http://jobview.monster.com/jr-software-engineer-job-burlington-ma-us-183070536.aspx?mescoid=1500127001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;18&#39;});; clickJobTitle(&#39;plid=893&amp;pcid=660&amp;poccid=11904&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Jr Software Engineer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xworkableukx_Sefas Innovation, Inc.&quot;,&quot;eVar31&quot;:&quot;Burlington_MA_&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-17T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Jr Software Engineer"><span itemprop="title">Jr Software Engineer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-sefas-innovation__2c-inc__2e.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;18&#39;});" rel="nofollow" title="Sefas Innovation, Inc."><span itemprop="name">Sefas Innovation, Inc.</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-burlington,-ma.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;18&#39;});" title="Burlington, MA"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Burlington, MA
            <meta itemprop="addressLocality" content="Burlington" />
            <meta itemprop="addressRegion" content="MA" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-17T12:00" itemprop="datePosted">5 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="We are growing strong and fast and we have an immediate opening for a Junior Software  Engineer. This position will be located in Burlington, MA. Additional information on the company is available at

We provide you with initial training on our ......" />
                    <meta itemprop="url" content="http://jobview.monster.com/jr-software-engineer-job-burlington-ma-us-183070536.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xAquesstx" data-m_impr_j_jawsid="230547261" data-m_impr_j_jobid="183080083" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="33.8365" data-m_impr_j_lid="950" data-m_impr_j_long="-84.3881" data-m_impr_j_occid="12005" data-m_impr_j_p="19" data-m_impr_j_postingid="e708d9b9-aeb1-4c02-864b-41a2f49d4e13" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="9a53a71f-98ce-4419-b2a8-55dedc6c3d4f" href="http://jobview.monster.com/lamp-software-engineer-job-atlanta-ga-us-183080083.aspx?mescoid=1500129001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;19&#39;});; clickJobTitle(&#39;plid=950&amp;pcid=660&amp;poccid=12005&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;quot;,&quot;eVar25&quot;:&quot;LAMP Software Engineer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xAquesstx_Aquesst&quot;,&quot;eVar31&quot;:&quot;Atlanta_GA_30305&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-17T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="LAMP Software Engineer"><span itemprop="title">LAMP Software Engineer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-aquesst.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;19&#39;});" rel="nofollow" title="Aquesst"><span itemprop="name">Aquesst</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-atlanta,-ga.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;19&#39;});" title="Atlanta, GA, 30305"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Atlanta, GA
            <meta itemprop="addressLocality" content="Atlanta" />
            <meta itemprop="addressRegion" content="GA" />
            <meta itemprop="postalCode" content="30305" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-17T12:00" itemprop="datePosted">5 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Software Engineer

Full time opportunity in Buckhead!



Seeking a LAMP Software Engineer who loves writing code, working with cutting edge technology, and building powerful and easy-to-use software! Join this fun and smart startup team in Buckhead......." />
                    <meta itemprop="url" content="http://jobview.monster.com/lamp-software-engineer-job-atlanta-ga-us-183080083.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xholtepermx" data-m_impr_j_jawsid="228302588" data-m_impr_j_jobid="182651205" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="42.3584" data-m_impr_j_lid="453" data-m_impr_j_long="-71.0598" data-m_impr_j_occid="11970" data-m_impr_j_p="20" data-m_impr_j_postingid="5581f1c7-3fbe-424c-9c4e-922b6cbf2b62" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="7fd35025-3b63-4e98-84a4-1a45b1719583" href="http://jobview.monster.com/software-engineer-virtualization-job-boston-ma-us-182651205.aspx?mescoid=1500127001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;20&#39;});; clickJobTitle(&#39;plid=453&amp;pcid=660&amp;poccid=11970&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Software Engineer- Virtualization&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xholtepermx_Hollister Staffing&quot;,&quot;eVar31&quot;:&quot;Boston_MA_&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-19T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Software Engineer- Virtualization"><span itemprop="title">Software Engineer- Virtualization</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-hollister-staffing.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;20&#39;});" rel="nofollow" title="Hollister Staffing"><span itemprop="name">Hollister Staffing</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-boston,-ma.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;20&#39;});" title="Boston, MA"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Boston, MA
            <meta itemprop="addressLocality" content="Boston" />
            <meta itemprop="addressRegion" content="MA" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-19T12:00" itemprop="datePosted">3 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Software Engineer- VirtualizationSoftware Engineer- Virtualization

Our Boston-based client is looking for a Software Engineer with a heavy focus on Virtualization. The Senior Software Engineer will have the opportunity to work on networking, scalab......" />
                    <meta itemprop="url" content="http://jobview.monster.com/software-engineer-virtualization-job-boston-ma-us-182651205.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xkforcex" data-m_impr_j_jawsid="228277897" data-m_impr_j_jobid="182638389" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="40.7142" data-m_impr_j_lid="630" data-m_impr_j_long="-111.8914" data-m_impr_j_occid="11970" data-m_impr_j_p="21" data-m_impr_j_postingid="50e31fd2-b88d-4666-aa85-b7868b585c43" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="821bdb8c-3e67-408b-be36-85cac5f76d2d" href="http://jobview.monster.com/senior-ios-developer-job-salt-lake-city-ut-us-182638389.aspx?mescoid=1500127001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;21&#39;});; clickJobTitle(&#39;plid=630&amp;pcid=660&amp;poccid=11970&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Senior iOS Developer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xkforcex_Kforce Inc&quot;,&quot;eVar31&quot;:&quot;Salt Lake City_UT_84115&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-19T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Senior iOS Developer"><span itemprop="title">Senior iOS Developer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-kforce-professional-staffing.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;21&#39;});" title="Kforce Inc"><span itemprop="name">Kforce Inc</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-salt-lake-city,-ut.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;21&#39;});" title="Salt Lake City, UT, 84115"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Salt Lake City, UT
            <meta itemprop="addressLocality" content="Salt Lake City" />
            <meta itemprop="addressRegion" content="UT" />
            <meta itemprop="postalCode" content="84115" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-19T12:00" itemprop="datePosted">3 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="RESPONSIBILITIES:Kforce is looking for a Senior iOS Developer for one of our clients in Salt Lake City, Utah (UT). If you have a passion for all things iOS please apply.

REQUIREMENTS:
-  Advanced knowledge of iOS APIs, Swift, Xcode, and other st......" />
                    <meta itemprop="url" content="http://jobview.monster.com/senior-ios-developer-job-salt-lake-city-ut-us-182638389.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xholtepermx" data-m_impr_j_jawsid="228306213" data-m_impr_j_jobid="182652886" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="42.3584" data-m_impr_j_lid="453" data-m_impr_j_long="-71.0598" data-m_impr_j_occid="11970" data-m_impr_j_p="22" data-m_impr_j_postingid="4663e548-8cf5-468c-aef1-1da49929d408" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="e4b5b090-4705-4141-a396-01b1779fba21" href="http://jobview.monster.com/sql-database-developer-job-boston-ma-us-182652886.aspx?mescoid=1500142001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;22&#39;});; clickJobTitle(&#39;plid=453&amp;pcid=660&amp;poccid=11970&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;SQL Database Developer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xholtepermx_Hollister Staffing&quot;,&quot;eVar31&quot;:&quot;Boston_MA_&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-19T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="SQL Database Developer"><span itemprop="title">SQL Database Developer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-hollister-staffing.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;22&#39;});" rel="nofollow" title="Hollister Staffing"><span itemprop="name">Hollister Staffing</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-boston,-ma.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;22&#39;});" title="Boston, MA"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Boston, MA
            <meta itemprop="addressLocality" content="Boston" />
            <meta itemprop="addressRegion" content="MA" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-19T12:00" itemprop="datePosted">3 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="SQL Database DeveloperSQL Database Developer

Our client, an industry-leading tech start-up based in Boston, is seeking a SQL Database Developer to join their Database group! This is a mission-critical position, perfect for someone who loves working......" />
                    <meta itemprop="url" content="http://jobview.monster.com/sql-database-developer-job-boston-ma-us-182652886.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xgen10x" data-m_impr_j_jawsid="230934769" data-m_impr_j_jobid="183182189" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="41.689" data-m_impr_j_lid="406" data-m_impr_j_long="-93.7182" data-m_impr_j_occid="12005" data-m_impr_j_p="23" data-m_impr_j_postingid="3bac5a2e-89b9-46a2-bf15-58105d7be8ff" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="78227ce0-1678-4cb9-b15e-2ca0b32b9cdc" href="http://jobview.monster.com/senior-software-engineer-encirca-job-johnston-ia-us-183182189.aspx?mescoid=1500127001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;23&#39;});; clickJobTitle(&#39;plid=406&amp;pcid=660&amp;poccid=12005&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Senior Software Engineer  - Encirca&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xgen10x_Genesis10&quot;,&quot;eVar31&quot;:&quot;Johnston_IA_50131&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-19T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Senior Software Engineer  - Encirca"><span itemprop="title">Senior Software Engineer  - Encirca</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-genesis10.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;23&#39;});" title="Genesis10"><span itemprop="name">Genesis10</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-johnston,-ia.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;23&#39;});" title="Johnston, IA, 50131"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Johnston, IA
            <meta itemprop="addressLocality" content="Johnston" />
            <meta itemprop="addressRegion" content="IA" />
            <meta itemprop="postalCode" content="50131" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-19T12:00" itemprop="datePosted">3 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Genesis10 is currently seeking a Senior Software Engineer for DIRECT HIRE – FULLTIME EMPLOYEE opportunity in Johnston, Iowa.

NO C2C
This is a DIRECT HIRE position.
 MUST be able to attend FACE TO FACE (IN PERSON) interview in Des Moines, Iowa

De......" />
                    <meta itemprop="url" content="http://jobview.monster.com/senior-software-engineer-encirca-job-johnston-ia-us-183182189.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="660" data-m_impr_j_coc="xholtepermx" data-m_impr_j_jawsid="228311338" data-m_impr_j_jobid="182655103" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="42.3584" data-m_impr_j_lid="453" data-m_impr_j_long="-71.0598" data-m_impr_j_occid="11979" data-m_impr_j_p="24" data-m_impr_j_postingid="31365dea-0432-49b0-bb6d-d50985a0bdcf" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="98c31160-371b-4a33-85c5-00091abe95c6" href="http://jobview.monster.com/data-scientist-job-boston-ma-us-182655103.aspx?mescoid=1500152001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;24&#39;});; clickJobTitle(&#39;plid=453&amp;pcid=660&amp;poccid=11979&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;Data Scientist&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xholtepermx_Hollister Staffing&quot;,&quot;eVar31&quot;:&quot;Boston_MA_&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-19T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="Data Scientist"><span itemprop="title">Data Scientist</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-hollister-staffing.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;24&#39;});" rel="nofollow" title="Hollister Staffing"><span itemprop="name">Hollister Staffing</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-boston,-ma.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;24&#39;});" title="Boston, MA"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Boston, MA
            <meta itemprop="addressLocality" content="Boston" />
            <meta itemprop="addressRegion" content="MA" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-19T12:00" itemprop="datePosted">3 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Data ScientistData Scientist

Are you inquisitive and creative? Do you enjoy taking on challenging data questions and coming up with the tools that help people answer them? Then we think you should apply to this position...
 Our client is a professi......" />
                    <meta itemprop="url" content="http://jobview.monster.com/data-scientist-job-boston-ma-us-182655103.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
        <div class="js_result_container clearfix primary">
            <span class="unseen-job-marker">New</span>
            <div class="applied-overlay">
                <div class="applied">
                    <i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span>
                </div>
            </div>
            <article class="js_result_row" itemtype="http://schema.org/JobPosting" itemscope>
                <div class="js_result_details">
                    <div class="js_result_details-left">
                        <div class="jobTitle">
                            <h2>
                                <a data-m_impr_a_placement_id="JSR2" data-m_impr_j_cid="4" data-m_impr_j_coc="xmacbrox" data-m_impr_j_jawsid="227810635" data-m_impr_j_jobid="182543385" data-m_impr_j_jpm="1" data-m_impr_j_jpt="1" data-m_impr_j_lat="39.8169" data-m_impr_j_lid="562" data-m_impr_j_long="-84.0506" data-m_impr_j_occid="11782" data-m_impr_j_p="25" data-m_impr_j_postingid="d54095f2-b666-4474-8494-764e9c3a4c36" data-m_impr_j_pvc="monster" data-m_impr_s_t="t" data-m_impr_uuid="8a56bf78-2ab7-4ffd-8d35-d097f98e10b7" href="http://jobview.monster.com/hitl-software-engineer-job-wright-patterson-afb-oh-us-182543385.aspx?mescoid=1500127001001&amp;jobPosition=1" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Title Link Click&#39;,&#39;eventLabel&#39;:&#39;25&#39;});; clickJobTitle(&#39;plid=562&amp;pcid=4&amp;poccid=11782&#39;,&#39;Python&#39;,&#39;&#39;); clickJobTitleSiteCat(&#39;{&quot;events.event48&quot;:&quot;true&quot;,&quot;eVar25&quot;:&quot;HITL Software Engineer&quot;,&quot;eVar66&quot;:&quot;Monster&quot;,&quot;eVar67&quot;:&quot;JSR2&quot;,&quot;eVar26&quot;:&quot;xmacbrox_MacAulay Brown Inc.&quot;,&quot;eVar31&quot;:&quot;Wright Patterson AFB_OH_45433&quot;,&quot;prop22&quot;:&quot;Full-Time&quot;,&quot;prop24&quot;:&quot;2017-04-17T12:00&quot;,&quot;eVar50&quot;:&quot;Duration&quot;}&#39;)" title="HITL Software Engineer"><span itemprop="title">HITL Software Engineer</span></a>
                            </h2>
                        </div>
                        <div class="company" itemtype="https://schema.org/Organization" itemscope itemprop="hiringOrganization">
<a href="https://www.monster.com/jobs/c-macaulay-brown.aspx" itemprop="url" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Company Link Click&#39;,&#39;eventLabel&#39;:&#39;25&#39;});" title="MacAulay Brown Inc."><span itemprop="name">MacAulay Brown Inc.</span>

</a>                            <i class="mdi mdi-wheelchair-accessibility" data-toggle="tooltip" data-placement="top" title="Handinamic"></i>
                            <i class="mdi mdi-equal" data-toggle="tooltip" data-placement="top" title="Prodiversit&#233;"></i>
                        </div>
                        <div class="row" itemtype="https://schema.org/Place" itemscope itemprop="jobLocation">
                            <div class="job-specs job-specs-location">
                                <i class="mdi mdi-map-marker-radius"></i>
                                <p>
<a href="https://www.monster.com/jobs/l-wright-patterson-afb,-oh.aspx" onMouseDown="dataLayer.push({&#39;eventCategory&#39;:&#39;LPF Job Listing&#39;,&#39;eventAction&#39;:&#39;Location Link Click&#39;,&#39;eventLabel&#39;:&#39;25&#39;});" title="Wright Patterson AFB, OH, 45433"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    Wright Patterson AFB, OH
            <meta itemprop="addressLocality" content="Wright Patterson AFB" />
            <meta itemprop="addressRegion" content="OH" />
            <meta itemprop="postalCode" content="45433" />
</span>
</a>                                </p>
                            </div>
                        </div>
                        <div class="row job-status-container">
                            <span href="#" class="fast-apply-text">Fast Apply</span>
                            <span class="save"><i class="mdi mdi-heart"></i><span class="save-text">Saved</span></span>
                            <!-- <span class="applied"><i class="mdi mdi-checkbox-marked-circle-outline"></i><span class="applied-text">Applied</span></span> -->
                        </div>
                    </div>
                    <div class="js_result_details-right">
                        <!-- logo if it exists: don't include wrapper div if it doesn't -->
                    </div>
                    <div class="job-specs job-specs-date">
                        <p><time datetime="2017-04-17T12:00" itemprop="datePosted">5 days ago</time></p>
                    </div>
                    <meta itemprop="description" content="Seeking a Electrical/Software Engineer with a background in Real-Time deterministic programming. This individual will be responsible for the development of real-time hardware-in-the-loop (HITL) simulations. The simulations use multiple physical node......" />
                    <meta itemprop="url" content="http://jobview.monster.com/hitl-software-engineer-job-wright-patterson-afb-oh-us-182543385.aspx" />
                    <meta itemprop="employmentType" content="Full-Time" />
                    <meta itemprop="industry" content="" />
                </div>
            </article>
        </div>
    </section>
<link rel="stylesheet" type="text/css" href="https://cdn.materialdesignicons.com/1.5.54/css/materialdesignicons.min.css" media="all">

        <div  id="twoColumnEmailWidget">

<input type="hidden" id="searchQuery" value="q=Python&amp;brd=1&amp;brd=2&amp;cy=US&amp;pg=40&amp;pp=25&amp;sort=rv.di.dt&amp;stp=TwoBoxBand" />
<input type="hidden" id="isLoggedIn" value="false" />
<input type="hidden" id="maxSaveSearchesAllowed" value="5" />
<input type="hidden" id="emailUrl" value="https://www.monster.com/jobs/emailjobs?q=Python&amp;page=40" />
<input type="hidden" id="isDynamicPage" value="True"/>

        <div class="widget popup-widget reveal">
            <i id="widget-popup-close-icon" class="fa fa-close close-icon"></i>
            <div class="widget-head">
                <div class="marked-title clearfix">
                    <i class="fa fa-envelope"></i>
                    <h3>Get Python jobs by e-mail</h3>
                </div>
            </div>
            <div class="widget-content savedSearches">
                <div class="messageholder">

                </div>
                <div class="widget-content-inner">
                    <span class="save_search_header">We&#39;ll keep looking and send you new jobs that match this search. It&#39;s that simple!</span>
                    <label for="emailAddress" class="sr-only">Enter Your Email Address</label>
                    <div>
                        <input type="text" value="" id="emailAddress2" name="emailAddress2" placeholder="Enter Your Email Address" class="form-control">
                        <button data-loading-text="<i class='fa fa-spinner fa-spin'></i>" type="button" title="Email me Jobs" value="Email Me Jobs" onclick="dataLayer.push({'eventCategory':'Sidebar Widgets','eventAction':'JSA','eventLabel':'Click Link in Widget'});; emailActionTabClick(this); " id="emailButton2">
                            Email me Jobs
                        </button>
                        <span id="privacyMSG" class="litRegPrivacy">
                            By continuing you agree to Monster's <a title="privacy policy" target="_blank" href="http://my.monster.com/Privacy/Default.aspx">Privacy Policy</a>, <a title="terms of use" target="_blank" href="http://my.monster.com/Terms/Default.aspx">Terms of Use</a> and <a title="use of cookies" target="_blank" href="http://inside.monster.com/cookie-info/inside2.aspx">Use of Cookies</a>.
                        </span>

                    </div>
                </div>
            </div>
        </div>



        </div>


    <input type="hidden" id="totalPages" value="40" />
    <input type="hidden" id="prevText" value="Previous" />
    <input type="hidden" id="nextText" value="Next" />
    <input type="hidden" id="currentPage" value="40" />
    <div class="pagingWrapper">
        <div class="paging">

        </div>
    </div>
    <script type="text/javascript">
        $(function() {
            InitializePagingResultSet();
        });
    </script>

                </div>































<script src="https://logs.jobs.com/impression_trackingv2.js" type="text/javascript"></script>
            </div>
        </div>
    </div>

                <div id="topPopupEmailCardViewWidget">

                </div>


	                </div>
	                <!-- Main content ends -->
	            </div><!-- Matter ends -->
	        </div><!-- Mainbar ends -->
	    </div>
	    <div class="clearfix"></div>
	    <!-- Footer -->
        <!-- Footer starts -->


        <div class="bannerAdFooter hidden-xs">

        </div>



<input type="hidden" id="envType" value="Production" />
<input type="hidden" id="version" value="1.0.0.0" />


    <footer role="contentinfo" class="new-footer">
        <div class="container">
            <a class="m-logo" href="https://www.monster.com" title="Go to Monster home"><img alt="Monster logo" src="https://securemedia.newjobs.com/niche/images/niche-footer-m.gif" /></a>
        <!-- Desktop view -->
        <div class="row hidden-xs">
            <ul class="col-sm-2 clearfix">
                <li><h3>For Job Seekers</h3></li>
                <li><a href="https://www.monster.com/jobs/">Find Jobs</a></li>
                <li><a href="http://resume.monster.com">Upload Resume</a></li>
                <li><a href="https://www.monster.com/sitemap" title="Job Seeker Site Map">Site Map</a></li>
                <li><a onclick="window.open(this.href, 'pop', 'toolbar=no,directories=no,location=no,status=yes,menubar=no,resizable=yes,scrollbars=yes,width=995,height=575'); return false;" href='https://monster.secure.force.com/ekb/EKBHome?brand=seeker' title="Job Seeker Help">Help</a></li>
            </ul>
            <ul class="col-sm-2 clearfix">
                <li><h3>For Employers</h3></li>
                <li><a href="http://hiring.monster.com">Post Jobs</a></li>
                <li><a href="http://hiring.monster.com/recruitment/Resume-Search-Database.aspx">Search Resumes</a></li>
                <li><a href="http://advertising.monster.com/">Advertise with us</a></li>
                <li><a href="http://hiring.monster.com/sitemap.aspx" title="Employer Site Map">Site Map</a></li>
                <li><a onclick="window.open(this.href, 'pop', 'toolbar=no,directories=no,location=no,status=yes,menubar=no,resizable=yes,scrollbars=yes,width=995,height=575'); return false;" href='https://monster.secure.force.com/ekb/EKBHome?brand=monster_usen' title="Employer Help">Help</a></li>
            </ul>
            <ul class="col-sm-2 clearfix">
                <li><h3>About Us</h3></li>
                <li><a href="https://www.monster.com/about">About Monster</a></li>
                <li><a href="https://www.monster.com/about/work-for-us">Work for Monster</a></li>
                <li><a href="http://partner.monster.com/">Partner with Us</a></li>
                <li><a href="http://ir.monster.com/phoenix.zhtml?c=110723&amp;p=irol-irhome">Investor Relations</a></li>
                <li><a href="https://www.monster.com/geo/siteselection">Monster International</a></li>
            </ul>
            <ul class="col-sm-2 clearfix">
                <li><h3>Helpful Resources</h3></li>
                <li><a onclick="window.open(this.href, 'pop', 'toolbar=no,directories=no,location=no,status=yes,menubar=no,resizable=yes,scrollbars=yes,width=995,height=575'); return false;" href='https://monster.secure.force.com/ekb/EKBContactUs?brand=seeker' title="Contact Us Popup">Contact Us</a></li>
                <li><a href="http://inside.monster.com/terms-of-use">Terms of Use</a></li>
                <li><a href="http://inside.monster.com/privacy/home.aspx">Privacy Center</a></li>
                <li><a href="http://inside.monster.com/security-center/home.aspx">Security Center</a></li>
                <li><a href="http://inside.monster.com/accessibility">Accessibility Center</a></li>
                <li><a href="http://preferences.truste.com/2.0/?type=monster&amp;affiliateId=155" rel="nofollow">AdChoices <i class="iconAdChoices"></i></a></li>
            </ul>
            <ul class="col-sm-2 clearfix">
                <li><h3>Find Jobs</h3></li>
                <li><a href="https://www.monster.com/jobs/">Jobs in US</a></li>
                <li><a href="https://www.monster.ca/jobs/">Jobs in Canada</a></li>
                <li><a href="https://www.monster.co.uk/jobs/">Jobs in UK</a></li>
                <li><a href="https://www.monster.fr/emploi/">Emplois en France</a></li>
                <li><a href="https://www.monster.de/jobs/">Jobs in Deutschland </a></li>
                <li><a href="https://www.monsterboard.nl/vacatures/">Vacatures in Nederland</a></li>
            </ul>
        </div>
        <!-- Mobile view -->
        <div class="row visible-xs">
            <ul class="col-xs-12 clearfix">
                <li><a href="https://www.monster.com/jobs/">Find Jobs</a></li>
                <li><a href="http://hiring.monster.com">Post Jobs</a></li>
                <li><a href="https://www.monster.com/about">About Monster</a></li>
               <li><a onclick="window.open(this.href, 'pop', 'toolbar=no,directories=no,location=no,status=yes,menubar=no,resizable=yes,scrollbars=yes,width=681,height=1053'); return false;" href='https://monster.secure.force.com/ekb/EKBContactUs?brand=seeker' title="Contact Us Popup">Contact Us</a></li>
                <li><a href="http://inside.monster.com/terms-of-use">Terms of Use</a></li>
                <li><a href="http://inside.monster.com/privacy/home.aspx">Privacy Center</a></li>
                <li><a href="http://inside.monster.com/security-center/home.aspx">Security Center</a></li>
            </ul>
        </div>
        <div class="findSocial">
            <h3>Find us on <a href="http://career-services.monster.com/social-media/home.aspx">social media</a>:</h3>
            <a class="fa fa-google-plus" href="https://plus.google.com/+monster" target="_blank"><span class="sr-only">Google Plus</span></a>
            <a class="fa fa-facebook" href="https://www.facebook.com/monster" target="_blank"><span class="sr-only">Facebook</span></a>
            <a class="fa fa-twitter" href="https://twitter.com/Monster" target="_blank"><span class="sr-only">Twitter</span></a>
            <a class="fa fa-instagram" href="https://instagram.com/monster" target="_blank"><span class="sr-only">Instagram</span></a>
            <a class="fa fa-youtube" href="https://www.youtube.com/monster" target="_blank"><span class="sr-only">YouTube</span></a>
        </div>
        <p class="copyrights">
            Copyright &copy; 2016 - <a href="https://www.monster.com/">Monster Worldwide</a>
        </p>
        <p class="patents">
            <span class="hidden-xs">U.S. Patents No. 7,599,930 B1; 7,827,125 and 7,836,060 - </span>Looking for <a href="http://www.monsterproducts.com/" target="_blank" rel="nofollow">Monster Cable</a>?
         - V: 2017.7.0.16-308</p>

        </div>
    </footer>



        <!-- Footer ends -->
    </div>
    <!-- Scroll to top -->
    <span class="totop"><a href="#"><i class="fa fa-chevron-up"></i></a></span>
    <div class="hide">



<div style="display:none;"></div>












    </div>
   </body>
</html>
"""