{% load staticfiles %}
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8" />
  <link rel="apple-touch-icon" sizes="76x76" href="../assets/img/apple-icon.png">
  <link rel="icon" type="image/png" href="../assets/img/favicon.png">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
  <title>
    Hairways Salon Management Software | Manage your salon, customer appointments and to be ranked as one of the best salons in town
  </title>
  <meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0, shrink-to-fit=no' name='viewport' />
  <!--     Fonts and icons     -->
  <link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Roboto+Slab:400,700|Material+Icons" />
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/latest/css/font-awesome.min.css">
  <!-- CSS Files -->
  <link href="{% static 'css/assets/css/material-dashboard.css' %}" rel="stylesheet" />
  <!-- CSS Just for demo purpose, don't include it in your project -->
<!--   <link href="../assets/demo/demo.css" rel="stylesheet" /> -->

<style type="text/css">
  body {
      color: #566787;
  background: #f5f5f5;
  font-family: 'Varela Round', sans-serif;
  font-size: 13px;
}
.table-wrapper {
      background: #fff;
      padding: 20px 25px;
      margin: 30px 0;
  border-radius: 3px;
      box-shadow: 0 1px 1px rgba(0,0,0,.05);
  }

.table-title .btn {
  color: #fff;
  float: right;
  font-size: 13px;
  border: none;
  min-width: 50px;
  border-radius: 2px;
  border: none;
  outline: none !important;
  margin-left: 10px;
}
.table-title .btn i {
  float: left;
  font-size: 21px;
  margin-right: 5px;
}
.table-title .btn span {
  float: left;
  margin-top: 2px;
}
  table.table tr th, table.table tr td {
      border-color: #e9e9e9;
  padding: 12px 15px;
  vertical-align: middle;
  }
table.table tr th:first-child {
  width: 60px;
}
table.table tr th:last-child {
  width: 100px;
}
  table.table-striped tbody tr:nth-of-type(odd) {
    background-color: #fcfcfc;
}
table.table-striped.table-hover tbody tr:hover {
  background: #f5f5f5;
}
  table.table th i {
      font-size: 13px;
      margin: 0 5px;
      cursor: pointer;
  }
  table.table td:last-child i {
  opacity: 0.9;
  font-size: 22px;
      margin: 0 5px;
  }
table.table td a {
  font-weight: bold;
  color: #566787;
  display: inline-block;
  text-decoration: none;
  outline: none !important;
}
table.table td a:hover {
  color: #2196F3;
}
table.table td a.edit {
      color: #FFC107;
  }
  table.table td a.delete {
      color: #F44336;
  }
  table.table td i {
      font-size: 19px;
  }
table.table .avatar {
  border-radius: 50%;
  vertical-align: middle;
  margin-right: 10px;
}
  .pagination {
      float: right;
      margin: 0 0 5px;
  }
  .pagination li a {
      border: none;
      font-size: 13px;
      min-width: 30px;
      min-height: 30px;
      color: #999;
      margin: 0 2px;
      line-height: 30px;
      border-radius: 2px !important;
      text-align: center;
      padding: 0 6px;
  }
  .pagination li a:hover {
      color: #666;
  }
  .pagination li.active a, .pagination li.active a.page-link {
      background: #03A9F4;
  }
  .pagination li.active a:hover {
      background: #0397d6;
  }
.pagination li.disabled i {
      color: #ccc;
  }
  .pagination li i {
      font-size: 16px;
      padding-top: 6px
  }
  .hint-text {
      float: left;
      margin-top: 10px;
      font-size: 13px;
  }
/* Custom checkbox */
.custom-checkbox {
  position: relative;
}
.custom-checkbox input[type="checkbox"] {
  opacity: 0;
  position: absolute;
  margin: 5px 0 0 3px;
  z-index: 9;
}
.custom-checkbox label:before{
  width: 18px;
  height: 18px;
}
.custom-checkbox label:before {
  content: '';
  margin-right: 10px;
  display: inline-block;
  vertical-align: text-top;
  background: white;
  border: 1px solid #bbb;
  border-radius: 2px;
  box-sizing: border-box;
  z-index: 2;
}
.custom-checkbox input[type="checkbox"]:checked + label:after {
  content: '';
  position: absolute;
  left: 6px;
  top: 3px;
  width: 6px;
  height: 11px;
  border: solid #000;
  border-width: 0 3px 3px 0;
  transform: inherit;
  z-index: 3;
  transform: rotateZ(45deg);
}
.custom-checkbox input[type="checkbox"]:checked + label:before {
  border-color: #03A9F4;
  background: #03A9F4;
}
.custom-checkbox input[type="checkbox"]:checked + label:after {
  border-color: #fff;
}
.custom-checkbox input[type="checkbox"]:disabled + label:before {
  color: #b8b8b8;
  cursor: auto;
  box-shadow: none;
  background: #ddd;
}
/* Modal styles */
.modal .modal-dialog {
  max-width: 400px;
}
.modal .modal-header, .modal .modal-body, .modal .modal-footer {
  padding: 20px 30px;
}
.modal .modal-content {
  border-radius: 3px;
}
.modal .modal-footer {
  background: #ecf0f1;
  border-radius: 0 0 3px 3px;
}
  .modal .modal-title {
      display: inline-block;
  }
.modal .form-control {
  border-radius: 2px;
  box-shadow: none;
  border-color: #dddddd;
}
.modal textarea.form-control {
  resize: vertical;
}
.modal .btn {
  border-radius: 2px;
  min-width: 100px;
}
.modal form label {
  font-weight: normal;
}
</style>

</head>

<body class="light-edition">
  <div class="wrapper ">
    <div class="sidebar"ata-color="purple" data-background-color="black" data-image="{% static 'css/assets/img/sidebar-2.jpg' %}">
      <!--
        Tip 1: You can change the color of the sidebar using: data-color="purple | azure | green | orange | danger"

        Tip 2: you can also add an image using data-image tag
    -->
      <div class="logo">
        <a href="index.html" class="simple-text logo-normal">
          Hairways
        </a>
      </div>
      <div class="sidebar-wrapper">
        <ul class="nav">
          <li class="nav-item">
            <a class="nav-link" href="/dashboard/">
              <i class="material-icons">dashboard</i>
              <p>Dashboard</p>
            </a>
          </li>
          <li class="nav-item ">
            <a class="nav-link" href="/user/">
              <i class="material-icons">person</i>
              <p>User Profile</p>
            </a>
          </li>
          <li class="nav-item ">
             <a class="nav-link" href="/productsServices/">
              <i class="material-icons">content_paste</i>
              <p>Products & Services</p>
            </a>
          </li>
          <li class="nav-item ">
             <a class="nav-link" href="/staffClients/">
              <i class="material-icons">library_books</i>
              <p>Staff & Clients</p>
            </a>
          </li>
          <li class="nav-item ">
            <a class="nav-link" href="/map/">
              <i class="material-icons">location_ons</i>
              <p>Map your Salon</p>
            </a>
          </li>
          <li class="nav-item ">
            <a class="nav-link" href="/calendar/">
              <i class="material-icons">notifications</i>
              <p>Calendar</p>
            </a>

          <li class="nav-item active-pro ">
                <a class="nav-link" href="/upgrade/">
                    <i class="material-icons">unarchive</i>
                    <p>Premium Services</p>
                </a>
            </li>
        </ul>
      </div>
    </div>
    <div class="main-panel">
      <!-- Navbar -->
      <nav class="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top " id="navigation-example">
        <div class="container-fluid">
          <div class="navbar-wrapper">
            <a class="navbar-brand" href="javascript:void(0)">Staffs and Clients</a>
          </div>
          <button class="navbar-toggler" type="button" data-toggle="collapse" aria-controls="navigation-index" aria-expanded="false" aria-label="Toggle navigation" data-target="#navigation-example">
            <span class="sr-only">Toggle navigation</span>
            <span class="navbar-toggler-icon icon-bar"></span>
            <span class="navbar-toggler-icon icon-bar"></span>
            <span class="navbar-toggler-icon icon-bar"></span>
          </button>
          <div class="collapse navbar-collapse justify-content-end">


            <ul class="navbar-nav">

              <li class="nav-item">
                <a class="nav-link" href="dashboard.php">
                  <i class="material-icons">dashboard</i>
                  <p class="d-lg-none d-md-block">
                    Stats
                  </p>
                </a>

              <li class="nav-item dropdown">
                <a class="nav-link" href="javscript:void(0)" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                  <i class="material-icons">person</i>
                  <p class="d-lg-none d-md-block">
                    Account
                  </p>
                </a>
                <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdownMenuLink">
                  <a class="dropdown-item" href="user.php">User profile</a>
                  <a class="dropdown-item" href="../index.html">Log out</a>

                </div>
                </a>
              </li>
            </ul>
            </ul>
          </div>
        </div>
      </nav>
      <!-- End Navbar -->
      <div class="content">
        <div class="container-fluid">
          <div class="row">
            <div class="col-md-12">     <!--   // START OF CLIENTS SECTION -->
              <div class="card">
                <div class="card-header card-header-primary">
                  <div class="table-title">
                      <div class="row">
                          <div class="col-sm-7">
                						<h2>Manage <b>Clients</b></h2>
                					</div>
                					<div class="col-sm-5">
                						<a href="#addEmployeeModal" class="btn btn-success" data-toggle="modal"><i class="material-icons">&#xE147;</i> <span>Add New Employee</span></a>
                						<a href="#deleteEmployeeModal" class="btn btn-danger" data-toggle="modal"><i class="material-icons">&#xE15C;</i> <span>Delete</span></a>
                					</div>
                      </div>
                  </div>
                </div>

                <div class="card-body">
                  <div class="container">
                    <div class="table-wrapper">
                        <table class="table table-striped table-hover">
                          <thead>
                            <tr>
                  						<th>
                  							<span class="custom-checkbox">
                  								<input type="checkbox" id="selectAll">
                  								<label for="selectAll"></label>
                  							</span>
                  						</th>
                              <th>Name</th>
                              <th>Email</th>
            						      <th>Address</th>
                              <th>Phone</th>
                              <th>Actions</th>
                            </tr>
                            </thead>
                            <tbody>
                              <tr>
            						        <td>
                    							<span class="custom-checkbox">
                    								<input type="checkbox" id="checkbox1" name="options[]" value="1">
                    								<label for="checkbox1"></label>
                    							</span>
            						        </td>
                                <td>Thomas Hardy</td>
                                <td>thomashardy@mail.com</td>
            						        <td>89 Chiaroscuro Rd, Portland, USA</td>
                                <td>(171) 555-2222</td>
                                <td>
                                  <a href="#editEmployeeModal" class="edit" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Edit">&#xE254;</i></a>
                                  <a href="#deleteEmployeeModal" class="delete" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Delete">&#xE872;</i></a>
                                </td>
                              </tr>
                              <tr>
            						        <td>
                    							<span class="custom-checkbox">
                    								<input type="checkbox" id="checkbox2" name="options[]" value="1">
                    								<label for="checkbox2"></label>
                    							</span>
                    						</td>
                                  <td>Dominique Perrier</td>
                                  <td>dominiqueperrier@mail.com</td>
            						          <td>Obere Str. 57, Berlin, Germany</td>
                                  <td>(313) 555-5735</td>
                                  <td>
                                    <a href="#editEmployeeModal" class="edit" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Edit">&#xE254;</i></a>
                                    <a href="#deleteEmployeeModal" class="delete" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Delete">&#xE872;</i></a>
                                  </td>
                              </tr>
                    					<tr>
                    						<td>
                    							<span class="custom-checkbox">
                    								<input type="checkbox" id="checkbox3" name="options[]" value="1">
                    								<label for="checkbox3"></label>
                    							</span>
                    						</td>
                                <td>Maria Anders</td>
                                <td>mariaanders@mail.com</td>
            						        <td>25, rue Lauriston, Paris, France</td>
                                <td>(503) 555-9931</td>
                                <td>
                                  <a href="#editEmployeeModal" class="edit" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Edit">&#xE254;</i></a>
                                  <a href="#deleteEmployeeModal" class="delete" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Delete">&#xE872;</i></a>
                                </td>
                              </tr>
                              <tr>
            						        <td>
            							        <span class="custom-checkbox">
            								        <input type="checkbox" id="checkbox4" name="options[]" value="1">
            								        <label for="checkbox4"></label>
                    							</span>
                    						</td>
                                <td>Fran Wilson</td>
                                <td>franwilson@mail.com</td>
            						        <td>C/ Araquil, 67, Madrid, Spain</td>
                                <td>(204) 619-5731</td>
                                <td>
                                  <a href="#editEmployeeModal" class="edit" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Edit">&#xE254;</i></a>
                                  <a href="#deleteEmployeeModal" class="delete" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Delete">&#xE872;</i></a>
                                </td>
                              </tr>
                    					<tr>
                    						<td>
                    							<span class="custom-checkbox">
                    								<input type="checkbox" id="checkbox5" name="options[]" value="1">
                    								<label for="checkbox5"></label>
                    							</span>
                    						</td>
                                  <td>Martin Blank</td>
                                  <td>martinblank@mail.com</td>
            						          <td>Via Monte Bianco 34, Turin, Italy</td>
                                  <td>(480) 631-2097</td>
                                  <td>
                                    <a href="#editEmployeeModal" class="edit" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Edit">&#xE254;</i></a>
                                    <a href="#deleteEmployeeModal" class="delete" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Delete">&#xE872;</i></a>
                                  </td>
                                </tr>
                            </tbody>
                        </table>

            			<div class="clearfix">
                    <div class="hint-text">Showing <b>5</b> out of <b>25</b> entries</div>
                      <ul class="pagination">
                        <li class="page-item disabled"><a href="#">Previous</a></li>
                        <li class="page-item"><a href="#" class="page-link">1</a></li>
                        <li class="page-item"><a href="#" class="page-link">2</a></li>
                        <li class="page-item active"><a href="#" class="page-link">3</a></li>
                        <li class="page-item"><a href="#" class="page-link">4</a></li>
                        <li class="page-item"><a href="#" class="page-link">5</a></li>
                        <li class="page-item"><a href="#" class="page-link">Next</a></li>
                      </ul>
                    </div>
                  </div>
                </div>

  <!-- Edit Modal HTML -->
              	<div id="addEmployeeModal" class="modal fade">
              		<div class="modal-dialog">
              			<div class="modal-content">
              				<form>
              					<div class="modal-header">
              						<h4 class="modal-title">Add Employee</h4>
              						<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
              					</div>
              					<!-- <div class="modal-body">
              						<div class="form-group">
              							<label>Name</label>
              							<input type="text" class="form-control" required>
              						</div>
              						<div class="form-group">
              							<label>Email</label>
              							<input type="email" class="form-control" required>
              						</div>
              						<div class="form-group">
              							<label>Address</label>
              							<textarea class="form-control" required></textarea>
              						</div>
              						<div class="form-group">
              							<label>Phone</label>
              							<input type="text" class="form-control" required>
              						</div>
              					</div> -->

                        <form action="" method="POST">
                        {{ crsf_token }}
                        {{ form }}

              					<div class="modal-footer">
              						<input type="button" class="btn btn-default" data-dismiss="modal" value="Cancel">
              						<input type="submit" class="btn btn-success" value="Add">
              					</div>
              				</form>
              			</div>
              		</div>
              	</div>

              	<!-- Edit Modal HTML -->
              	<div id="editEmployeeModal" class="modal fade">
              		<div class="modal-dialog">
              			<div class="modal-content">
              				<form>
              					<div class="modal-header">
              						<h4 class="modal-title">Edit Employee</h4>
              						<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
              					</div>
              					<div class="modal-body">
              						<div class="form-group">
              							<label>Name</label>
              							<input type="text" class="form-control" required>
              						</div>
              						<div class="form-group">
              							<label>Email</label>
              							<input type="email" class="form-control" required>
              						</div>
              						<div class="form-group">
              							<label>Address</label>
              							<textarea class="form-control" required></textarea>
              						</div>
              						<div class="form-group">
              							<label>Phone</label>
              							<input type="text" class="form-control" required>
              						</div>
              					</div>
              					<div class="modal-footer">
              						<input type="button" class="btn btn-default" data-dismiss="modal" value="Cancel">
              						<input type="submit" class="btn btn-info" value="Save">
              					</div>
              				</form>
              			</div>
              		</div>
              	</div>

              	<!-- Delete Modal HTML -->
              	<div id="deleteEmployeeModal" class="modal fade">
              		<div class="modal-dialog">
              			<div class="modal-content">
              				<form>
              					<div class="modal-header">
              						<h4 class="modal-title">Delete Employee</h4>
              						<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
              					</div>
              					<div class="modal-body">
              						<p>Are you sure you want to delete these Records?</p>
              						<p class="text-warning"><small>This action cannot be undone.</small></p>
              					</div>
              					<div class="modal-footer">
              						<input type="button" class="btn btn-default" data-dismiss="modal" value="Cancel">
              						<input type="submit" class="btn btn-danger" value="Delete">
              					</div>
              				</form>
              			</div>
              		</div>
              	</div>
              </div>
            </div>
          </div>

          <!-- END OF CLIENTS SECTION -->


          <!-- START OF EMPLOYEES SECTION -->
          <div class="col-md-12">
            <div class="card">
              <div class="card-header card-header-primary">
                <div class="table-title">
                    <div class="row">
                        <div class="col-sm-7">
                          <h2>Manage <b>Employees</b></h2>
                        </div>
                        <div class="col-sm-5">
                          <a href="#addEmployeeModal" class="btn btn-success" data-toggle="modal"><i class="material-icons">&#xE147;</i> <span>Add New Employee</span></a>
                          <a href="#deleteEmployeeModal" class="btn btn-danger" data-toggle="modal"><i class="material-icons">&#xE15C;</i> <span>Delete</span></a>
                        </div>
                    </div>
                </div>
              </div>

              <div class="card-body">
                <div class="container">
                  <div class="table-wrapper">
                      <table class="table table-striped table-hover">
                        <thead>
                          <tr>
                            <th>
                              <span class="custom-checkbox">
                                <input type="checkbox" id="selectAll">
                                <label for="selectAll"></label>
                              </span>
                            </th>
                            <th>Name</th>
                            <th>Email</th>
                            <th>Address</th>
                            <th>Phone</th>
                            <th>Actions</th>
                          </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td>
                                <span class="custom-checkbox">
                                  <input type="checkbox" id="checkbox1" name="options[]" value="1">
                                  <label for="checkbox1"></label>
                                </span>
                              </td>
                              <td>Thomas Hardy</td>
                              <td>thomashardy@mail.com</td>
                              <td>89 Chiaroscuro Rd, Portland, USA</td>
                              <td>(171) 555-2222</td>
                              <td>
                                <a href="#editEmployeeModal" class="edit" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Edit">&#xE254;</i></a>
                                <a href="#deleteEmployeeModal" class="delete" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Delete">&#xE872;</i></a>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <span class="custom-checkbox">
                                  <input type="checkbox" id="checkbox2" name="options[]" value="1">
                                  <label for="checkbox2"></label>
                                </span>
                              </td>
                                <td>Dominique Perrier</td>
                                <td>dominiqueperrier@mail.com</td>
                                <td>Obere Str. 57, Berlin, Germany</td>
                                <td>(313) 555-5735</td>
                                <td>
                                  <a href="#editEmployeeModal" class="edit" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Edit">&#xE254;</i></a>
                                  <a href="#deleteEmployeeModal" class="delete" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Delete">&#xE872;</i></a>
                                </td>
                            </tr>
                            <tr>
                              <td>
                                <span class="custom-checkbox">
                                  <input type="checkbox" id="checkbox3" name="options[]" value="1">
                                  <label for="checkbox3"></label>
                                </span>
                              </td>
                              <td>Maria Anders</td>
                              <td>mariaanders@mail.com</td>
                              <td>25, rue Lauriston, Paris, France</td>
                              <td>(503) 555-9931</td>
                              <td>
                                <a href="#editEmployeeModal" class="edit" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Edit">&#xE254;</i></a>
                                <a href="#deleteEmployeeModal" class="delete" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Delete">&#xE872;</i></a>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <span class="custom-checkbox">
                                  <input type="checkbox" id="checkbox4" name="options[]" value="1">
                                  <label for="checkbox4"></label>
                                </span>
                              </td>
                              <td>Fran Wilson</td>
                              <td>franwilson@mail.com</td>
                              <td>C/ Araquil, 67, Madrid, Spain</td>
                              <td>(204) 619-5731</td>
                              <td>
                                <a href="#editEmployeeModal" class="edit" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Edit">&#xE254;</i></a>
                                <a href="#deleteEmployeeModal" class="delete" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Delete">&#xE872;</i></a>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <span class="custom-checkbox">
                                  <input type="checkbox" id="checkbox5" name="options[]" value="1">
                                  <label for="checkbox5"></label>
                                </span>
                              </td>
                                <td>Martin Blank</td>
                                <td>martinblank@mail.com</td>
                                <td>Via Monte Bianco 34, Turin, Italy</td>
                                <td>(480) 631-2097</td>
                                <td>
                                  <a href="#editEmployeeModal" class="edit" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Edit">&#xE254;</i></a>
                                  <a href="#deleteEmployeeModal" class="delete" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Delete">&#xE872;</i></a>
                                </td>
                              </tr>
                          </tbody>
                      </table>

                <div class="clearfix">
                  <div class="hint-text">Showing <b>5</b> out of <b>25</b> entries</div>
                    <ul class="pagination">
                      <li class="page-item disabled"><a href="#">Previous</a></li>
                      <li class="page-item"><a href="#" class="page-link">1</a></li>
                      <li class="page-item"><a href="#" class="page-link">2</a></li>
                      <li class="page-item active"><a href="#" class="page-link">3</a></li>
                      <li class="page-item"><a href="#" class="page-link">4</a></li>
                      <li class="page-item"><a href="#" class="page-link">5</a></li>
                      <li class="page-item"><a href="#" class="page-link">Next</a></li>
                    </ul>
                  </div>
                </div>
              </div>

<!-- Edit Modal HTML -->
              <div id="addEmployeeModal" class="modal fade">
                <div class="modal-dialog">
                  <div class="modal-content">
                    <form>
                      <div class="modal-header">
                        <h4 class="modal-title">Add Employee</h4>
                        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                      </div>
                      <div class="modal-body">
                        <div class="form-group">
                          <label>Name</label>
                          <input type="text" class="form-control" required>
                        </div>
                        <div class="form-group">
                          <label>Email</label>
                          <input type="email" class="form-control" required>
                        </div>
                        <div class="form-group">
                          <label>Address</label>
                          <textarea class="form-control" required></textarea>
                        </div>
                        <div class="form-group">
                          <label>Phone</label>
                          <input type="text" class="form-control" required>
                        </div>
                      </div>
                      <div class="modal-footer">
                        <input type="button" class="btn btn-default" data-dismiss="modal" value="Cancel">
                        <input type="submit" class="btn btn-success" value="Add">
                      </div>
                    </form>
                  </div>
                </div>
              </div>

              <!-- Edit Modal HTML -->
              <div id="editEmployeeModal" class="modal fade">
                <div class="modal-dialog">
                  <div class="modal-content">
                    <form>
                      <div class="modal-header">
                        <h4 class="modal-title">Edit Employee</h4>
                        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                      </div>
                      <div class="modal-body">
                        <div class="form-group">
                          <label>Name</label>
                          <input type="text" class="form-control" required>
                        </div>
                        <div class="form-group">
                          <label>Email</label>
                          <input type="email" class="form-control" required>
                        </div>
                        <div class="form-group">
                          <label>Address</label>
                          <textarea class="form-control" required></textarea>
                        </div>
                        <div class="form-group">
                          <label>Phone</label>
                          <input type="text" class="form-control" required>
                        </div>
                      </div>
                      <div class="modal-footer">
                        <input type="button" class="btn btn-default" data-dismiss="modal" value="Cancel">
                        <input type="submit" class="btn btn-info" value="Save">
                      </div>
                    </form>
                  </div>
                </div>
              </div>

              <!-- Delete Modal HTML -->
              <div id="deleteEmployeeModal" class="modal fade">
                <div class="modal-dialog">
                  <div class="modal-content">
                    <form>
                      <div class="modal-header">
                        <h4 class="modal-title">Delete Employee</h4>
                        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                      </div>
                      <div class="modal-body">
                        <p>Are you sure you want to delete these Records?</p>
                        <p class="text-warning"><small>This action cannot be undone.</small></p>
                      </div>
                      <div class="modal-footer">
                        <input type="button" class="btn btn-default" data-dismiss="modal" value="Cancel">
                        <input type="submit" class="btn btn-danger" value="Delete">
                      </div>
                    </form>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- END OF EMPLOYEE SECTION -->

          </div>
        </div>
      </div>


        <footer class="footer">
        <div class="container-fluid">
          <nav class="float-left">
            <ul>
              <li>
                <a href="home.html">
                  Home
                </a>
              </li>
              <li>
                <a href="#">
                  About Us
                </a>
              </li>
              <li>
                <a href="#">
                  Blog
                </a>
              </li>
            </ul>
          </nav>
          <div class="copyright float-right" id="date">
        </div>
      </footer>

      <!-- SCRIPT FOR NEW TABLE -->

      <script type="text/javascript">
$(document).ready(function(){
	// Activate tooltip
	$('[data-toggle="tooltip"]').tooltip();

	// Select/Deselect checkboxes
	var checkbox = $('table tbody input[type="checkbox"]');
	$("#selectAll").click(function(){
		if(this.checked){
			checkbox.each(function(){
				this.checked = true;
			});
		} else{
			checkbox.each(function(){
				this.checked = false;
			});
		}
	});
	checkbox.click(function(){
		if(!this.checked){
			$("#selectAll").prop("checked", false);
		}
	});
});
</script>

      <!-- END OF TABLE SCRIPT -->


      <script>
        const x = new Date().getFullYear();
        let date = document.getElementById('date');
        date.innerHTML = '&copy; ' + x + date.innerHTML;
      </script>
    </div>
  </div>
  <div class="fixed-plugin">
    <div class="dropdown show-dropdown">
      <a href="#" data-toggle="dropdown">
        <i class="fa fa-cog fa-2x"> </i>
      </a>
      <ul class="dropdown-menu">
        <li class="header-title"> Sidebar Filters</li>
        <li class="adjustments-line">
          <a href="javascript:void(0)" class="switch-trigger active-color">
            <div class="badge-colors ml-auto mr-auto">
              <span class="badge filter badge-purple active" data-color="purple"></span>
              <span class="badge filter badge-azure" data-color="azure"></span>
              <span class="badge filter badge-green" data-color="green"></span>
              <span class="badge filter badge-warning" data-color="orange"></span>
              <span class="badge filter badge-danger" data-color="danger"></span>
            </div>
            <div class="clearfix"></div>
          </a>
        </li>
        <li class="header-title">Images</li>
        <li>
          <a class="img-holder switch-trigger" href="javascript:void(0)">
            <img src="{% static 'css/assets/img/sidebar-1.jpg' %}" alt="">
          </a>
        </li>
        <li class="active">
          <a class="img-holder switch-trigger" href="javascript:void(0)">
            <img src="{% static 'css/assets/img/sidebar-2.jpg' %}" alt="">
          </a>
        </li>
        <li>
          <a class="img-holder switch-trigger" href="javascript:void(0)">
            <img src="{% static 'css/assets/img/sidebar-3.jpg' %}" alt="">
          </a>
        </li>
        <li>
          <a class="img-holder switch-trigger" href="javascript:void(0)">
            <img src="{% static 'css/assets/img/sidebar-4.jpg' %}" alt="">
          </a>
        </li>

      </ul>
    </div>
  </div>
  <!--   Core JS Files   -->
  <script src="{% static 'css/assets/js/core/jquery.min.js' %}"></script>
  <script src="{% static 'css/assets/js/core/popper.min.js' %}"></script>
  <script src="{% static 'css/assets/js/core/bootstrap-material-design.min.js' %}"></script>
  <script src="https://unpkg.com/default-passive-events"></script>
  <script src="{% static 'css/assets/js/plugins/perfect-scrollbar.jquery.min.js' %}"></script>
  <!-- Place this tag in your head or just before your close body tag. -->
  <script async defer src="https://buttons.github.io/buttons.js"></script>
  <!--  Google Maps Plugin    -->
  <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_KEY_HERE"></script>
  <!-- Chartist JS -->
  <script src="{% static 'css/assets/js/plugins/chartist.min.js' %}"></script>
  <!--  Notifications Plugin    -->
  <script src="{% static 'css/assets/js/plugins/bootstrap-notify.js' %}"></script>
  <!-- Control Center for Material Dashboard: parallax effects, scripts for the example pages etc -->
  <script src="{% static 'css/assets/js/material-dashboard.js' %}"></script>
  <!-- Material Dashboard DEMO methods, don't include it in your project! -->
  <script src="{% static 'css/assets/demo/demo.js' %}"></script>
  <script>
    $(document).ready(function() {
      $().ready(function() {
        $sidebar = $('.sidebar');

        $sidebar_img_container = $sidebar.find('.sidebar-background');

        $full_page = $('.full-page');

        $sidebar_responsive = $('body > .navbar-collapse');

        window_width = $(window).width();

        $('.fixed-plugin a').click(function(event) {
          // Alex if we click on switch, stop propagation of the event, so the dropdown will not be hide, otherwise we set the  section active
          if ($(this).hasClass('switch-trigger')) {
            if (event.stopPropagation) {
              event.stopPropagation();
            } else if (window.event) {
              window.event.cancelBubble = true;
            }
          }
        });

        $('.fixed-plugin .active-color span').click(function() {
          $full_page_background = $('.full-page-background');

          $(this).siblings().removeClass('active');
          $(this).addClass('active');

          var new_color = $(this).data('color');

          if ($sidebar.length != 0) {
            $sidebar.attr('data-color', new_color);
          }

          if ($full_page.length != 0) {
            $full_page.attr('filter-color', new_color);
          }

          if ($sidebar_responsive.length != 0) {
            $sidebar_responsive.attr('data-color', new_color);
          }
        });

        $('.fixed-plugin .background-color .badge').click(function() {
          $(this).siblings().removeClass('active');
          $(this).addClass('active');

          var new_color = $(this).data('background-color');

          if ($sidebar.length != 0) {
            $sidebar.attr('data-background-color', new_color);
          }
        });

        $('.fixed-plugin .img-holder').click(function() {
          $full_page_background = $('.full-page-background');

          $(this).parent('li').siblings().removeClass('active');
          $(this).parent('li').addClass('active');


          var new_image = $(this).find("img").attr('src');

          if ($sidebar_img_container.length != 0 && $('.switch-sidebar-image input:checked').length != 0) {
            $sidebar_img_container.fadeOut('fast', function() {
              $sidebar_img_container.css('background-image', 'url("' + new_image + '")');
              $sidebar_img_container.fadeIn('fast');
            });
          }

          if ($full_page_background.length != 0 && $('.switch-sidebar-image input:checked').length != 0) {
            var new_image_full_page = $('.fixed-plugin li.active .img-holder').find('img').data('src');

            $full_page_background.fadeOut('fast', function() {
              $full_page_background.css('background-image', 'url("' + new_image_full_page + '")');
              $full_page_background.fadeIn('fast');
            });
          }

          if ($('.switch-sidebar-image input:checked').length == 0) {
            var new_image = $('.fixed-plugin li.active .img-holder').find("img").attr('src');
            var new_image_full_page = $('.fixed-plugin li.active .img-holder').find('img').data('src');

            $sidebar_img_container.css('background-image', 'url("' + new_image + '")');
            $full_page_background.css('background-image', 'url("' + new_image_full_page + '")');
          }

          if ($sidebar_responsive.length != 0) {
            $sidebar_responsive.css('background-image', 'url("' + new_image + '")');
          }
        });

        $('.switch-sidebar-image input').change(function() {
          $full_page_background = $('.full-page-background');

          $input = $(this);

          if ($input.is(':checked')) {
            if ($sidebar_img_container.length != 0) {
              $sidebar_img_container.fadeIn('fast');
              $sidebar.attr('data-image', '#');
            }

            if ($full_page_background.length != 0) {
              $full_page_background.fadeIn('fast');
              $full_page.attr('data-image', '#');
            }

            background_image = true;
          } else {
            if ($sidebar_img_container.length != 0) {
              $sidebar.removeAttr('data-image');
              $sidebar_img_container.fadeOut('fast');
            }

            if ($full_page_background.length != 0) {
              $full_page.removeAttr('data-image', '#');
              $full_page_background.fadeOut('fast');
            }

            background_image = false;
          }
        });

        $('.switch-sidebar-mini input').change(function() {
          $body = $('body');

          $input = $(this);

          if (md.misc.sidebar_mini_active == true) {
            $('body').removeClass('sidebar-mini');
            md.misc.sidebar_mini_active = false;

            $('.sidebar .sidebar-wrapper, .main-panel').perfectScrollbar();

          } else {

            $('.sidebar .sidebar-wrapper, .main-panel').perfectScrollbar('destroy');

            setTimeout(function() {
              $('body').addClass('sidebar-mini');

              md.misc.sidebar_mini_active = true;
            }, 300);
          }

          // we simulate the window Resize so the charts will get updated in realtime.
          var simulateWindowResize = setInterval(function() {
            window.dispatchEvent(new Event('resize'));
          }, 180);

          // we stop the simulation of Window Resize after the animations are completed
          setTimeout(function() {
            clearInterval(simulateWindowResize);
          }, 1000);

        });
      });
    });
  </script>
</body>

</html>
