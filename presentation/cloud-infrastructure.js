// Cloud Infrastructure Data Flow Animation - SVG Based

document.addEventListener('DOMContentLoaded', function() {
  // Animation sequence for data flow using SVG paths
  const flowSequence = [
    // User to CloudFront
    { path: '#path-user-cloudfront', delay: 0, duration: 2000 },
    // CloudFront to S3
    { path: '#path-cloudfront-s3', delay: 800, duration: 2000 },
    // User to ALB
    { path: '#path-user-alb', delay: 1600, duration: 2000 },
    // ALB to IGW
    { path: '#path-alb-igw', delay: 2400, duration: 2000 },
    // ALB to Public Subnets (parallel)
    { path: '#path-alb-subnet1', delay: 3200, duration: 2000 },
    { path: '#path-alb-subnet2', delay: 3300, duration: 2000 },
    { path: '#path-alb-subnet3', delay: 3400, duration: 2000 },
    // Public to Private Subnets
    { path: '#path-public-private1', delay: 4200, duration: 2000 },
    { path: '#path-public-private2', delay: 4300, duration: 2000 },
    { path: '#path-public-private3', delay: 4400, duration: 2000 },
    // Private Subnets to RDS
    { path: '#path-private-rds1', delay: 5200, duration: 2000 },
    { path: '#path-private-rds2', delay: 5300, duration: 2000 },
    { path: '#path-private-rds3', delay: 5400, duration: 2000 },
    // RDS Failover (continuous)
    { path: '#path-rds-failover1', delay: 6200, duration: 3000, continuous: true },
    { path: '#path-rds-failover2', delay: 6200, duration: 3000, continuous: true }
  ];

  // Function to activate a path
  function activatePath(selector) {
    const path = document.querySelector(selector);
    if (path) {
      path.classList.add('active');
      const length = path.getTotalLength();
      path.style.strokeDasharray = length + ' ' + length;
      path.style.strokeDashoffset = length;
    }
  }

  // Function to deactivate a path
  function deactivatePath(selector) {
    const path = document.querySelector(selector);
    if (path) {
      path.classList.remove('active');
    }
  }

  // Initialize all paths with stroke-dasharray
  document.querySelectorAll('.flow-path').forEach(path => {
    const length = path.getTotalLength();
    path.style.strokeDasharray = length + ' ' + length;
    path.style.strokeDashoffset = length;
  });

  // Start the animation sequence
  function startFlowAnimation() {
    flowSequence.forEach((flow) => {
      setTimeout(() => {
        activatePath(flow.path);
        
        // If not continuous, deactivate after duration
        if (!flow.continuous) {
          setTimeout(() => {
            deactivatePath(flow.path);
          }, flow.duration);
        }
      }, flow.delay);
    });
  }

  // Continuous animation loop
  function startContinuousFlow() {
    // Activate failover paths immediately and keep them active
    document.querySelectorAll('.flow-path.failover').forEach(path => {
      path.classList.add('active');
    });
    
    // Initial delay before starting main flow
    setTimeout(() => {
      startFlowAnimation();
      
      // Repeat the entire sequence every 8 seconds
      setInterval(() => {
        // Reset all paths (except continuous ones)
        const allPaths = document.querySelectorAll('.flow-path');
        allPaths.forEach(path => {
          if (!path.classList.contains('failover')) {
            path.classList.remove('active');
          }
        });
        
        // Restart animation after a brief pause
        setTimeout(() => {
          startFlowAnimation();
        }, 200);
      }, 8000);
    }, 1000);
  }

  // Initialize animations immediately
  setTimeout(() => {
    startContinuousFlow();
  }, 500);

  // Add hover effects to components
  const components = document.querySelectorAll('.service-box, .subnet-box, .rds-box, .integration-box');
  components.forEach(component => {
    component.addEventListener('mouseenter', function() {
      this.style.transition = 'all 0.3s ease';
    });
  });

  // RDS Active instance pulsing
  const activeRDS = document.querySelector('.rds-box.active');
  if (activeRDS) {
    setInterval(() => {
      activeRDS.style.animation = 'none';
      setTimeout(() => {
        activeRDS.style.animation = 'pulse 2s infinite';
      }, 10);
    }, 4000);
  }

});
