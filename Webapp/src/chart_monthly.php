 <script type="text/javascript" src="./assets/scripts/main.js"></script>
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>


    <script>
      function chart1(){
        <?php
        $query = "SELECT * FROM `tbl_attention`";
        $c1 = "[";
        $c2 = "[";
        $c3 = "[";

        if ($result = $mysqli->query($query)) {
            while ($row = $result->fetch_assoc()) {
              // echo "Raptor";
               $c1 = $c1.$row['Class_id'].",";
               $c2 = $c2.$row['Average_Attention'].",";
               

            }
          $result->free();
          $c1 = $c1."]\n";
          $c2 = $c2."]\n";
        

          }
         ?>
        var color = Chart.helpers.color;
        var barChartData = {
            labels: ['January', 'February', 'March', 'April', 'May', 'August','September','October','November','December'],
            datasets: [{
                label: 'Month',
                backgroundColor: color(window.chartColors.red).alpha(0.99).rgbString(),
                borderColor: window.chartColors.red,
                borderWidth: 1,
                data: <?php echo $c1;?>
            }, {
                label: 'Attention',
                backgroundColor: color(window.chartColors.blue).alpha(0.99).rgbString(),
                borderColor: window.chartColors.blue,
                borderWidth: 1,
                data: <?php echo $c2;?>
            }]

        };

        var ctx = document.getElementById('chart1').getContext('2d');
        window.myBar = new Chart(ctx, {
            type: 'bar',
            data: barChartData,
            options: {
                responsive: true,
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Area One'
                }
            }
        });
      }
      chart1();
    </script>