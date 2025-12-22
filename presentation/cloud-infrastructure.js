// Cloud Infrastructure Data Flow Animation - SVG Based

document.addEventListener('DOMContentLoaded', function() {
  // Animation sequence for data flow using CSS arrows
  const flowSequence = [
    // User to CloudFront
    { arrow: '.arrow-user-cloudfront', delay: 0, duration: 2000 },
    // CloudFront to S3
    { arrow: '.arrow-cloudfront-s3', delay: 800, duration: 2000 },
    // User to ALB
    { arrow: '.arrow-user-alb', delay: 1600, duration: 2000 },
    // ALB to IGW
    { arrow: '.arrow-alb-igw', delay: 2400, duration: 2000 },
    // ALB to Public Subnets (parallel)
    { arrow: '.arrow-alb-subnet1', delay: 3200, duration: 2000 },
    { arrow: '.arrow-alb-subnet2', delay: 3300, duration: 2000 },
    { arrow: '.arrow-alb-subnet3', delay: 3400, duration: 2000 },
    // Public to Private Subnets
    { arrow: '.arrow-public-private1', delay: 4200, duration: 2000 },
    { arrow: '.arrow-public-private2', delay: 4300, duration: 2000 },
    { arrow: '.arrow-public-private3', delay: 4400, duration: 2000 },
    // Private Subnets to RDS
    { arrow: '.arrow-private-rds1', delay: 5200, duration: 2000 },
    { arrow: '.arrow-private-rds2', delay: 5300, duration: 2000 },
    { arrow: '.arrow-private-rds3', delay: 5400, duration: 2000 },
    // RDS Failover (continuous)
    { arrow: '.arrow-rds-failover1', delay: 6200, duration: 3000, continuous: true },
    { arrow: '.arrow-rds-failover2', delay: 6200, duration: 3000, continuous: true }
  ];

  // Function to activate an arrow
  function activateArrow(selector) {
    const arrow = document.querySelector(selector);
    if (arrow) {
      arrow.classList.add('active');
    }
  }

  // Function to deactivate an arrow
  function deactivateArrow(selector) {
    const arrow = document.querySelector(selector);
    if (arrow) {
      arrow.classList.remove('active');
    }
  }

  // Start the animation sequence
  function startFlowAnimation() {
    flowSequence.forEach((flow) => {
      setTimeout(() => {
        activateArrow(flow.arrow);
        
        // If not continuous, deactivate after duration
        if (!flow.continuous) {
          setTimeout(() => {
            deactivateArrow(flow.arrow);
          }, flow.duration);
        }
      }, flow.delay);
    });
  }

  // Continuous animation loop
  function startContinuousFlow() {
    // Initial delay before starting
    setTimeout(() => {
      startFlowAnimation();
      
      // Repeat the entire sequence every 10 seconds
      setInterval(() => {
        // Reset all arrows (except continuous ones)
        const allArrows = document.querySelectorAll('.flow-arrow-line');
        allArrows.forEach(arrow => {
          if (!arrow.classList.contains('failover')) {
            arrow.classList.remove('active');
          }
        });
        
        // Restart animation after a brief pause
        setTimeout(() => {
          startFlowAnimation();
        }, 300);
      }, 10000);
    }, 1000);
  }

  // Position arrows dynamically based on component positions
  function positionArrows() {
    const awsBoundary = document.querySelector('.aws-cloud-boundary');
    if (!awsBoundary) return;
    
    const boundaryRect = awsBoundary.getBoundingClientRect();
    
    // User to CloudFront
    const userBox = document.querySelector('.user-box');
    const cloudfrontBox = document.querySelector('#cloudfront');
    if (userBox && cloudfrontBox) {
      const userRect = userBox.getBoundingClientRect();
      const cloudfrontRect = cloudfrontBox.getBoundingClientRect();
      const arrow = document.querySelector('.arrow-user-cloudfront');
      if (arrow) {
        const startX = userRect.left + userRect.width / 2 - boundaryRect.left;
        const startY = userRect.bottom - boundaryRect.top;
        const endX = cloudfrontRect.left + cloudfrontRect.width / 2 - boundaryRect.left;
        const endY = cloudfrontRect.top - boundaryRect.top;
        const length = Math.sqrt(Math.pow(endX - startX, 2) + Math.pow(endY - startY, 2));
        const angle = Math.atan2(endY - startY, endX - startX) * 180 / Math.PI;
        arrow.style.left = startX + 'px';
        arrow.style.top = startY + 'px';
        arrow.style.width = length + 'px';
        arrow.style.transform = `rotate(${angle}deg)`;
        arrow.style.transformOrigin = 'left center';
      }
    }
    
    // CloudFront to S3
    const s3Box = document.querySelector('#s3');
    if (cloudfrontBox && s3Box) {
      const s3Rect = s3Box.getBoundingClientRect();
      const arrow = document.querySelector('.arrow-cloudfront-s3');
      if (arrow) {
        const startX = cloudfrontRect.left + cloudfrontRect.width / 2 - boundaryRect.left;
        const startY = cloudfrontRect.bottom - boundaryRect.top;
        const endY = s3Rect.top - boundaryRect.top;
        arrow.style.left = startX + 'px';
        arrow.style.top = startY + 'px';
        arrow.style.width = (endY - startY) + 'px';
        arrow.style.transform = 'rotate(90deg)';
        arrow.style.transformOrigin = 'top center';
      }
    }
    
    // User to ALB
    const albBox = document.querySelector('#alb');
    if (userBox && albBox) {
      const albRect = albBox.getBoundingClientRect();
      const arrow = document.querySelector('.arrow-user-alb');
      if (arrow) {
        const startX = userRect.left + userRect.width / 2 - boundaryRect.left;
        const startY = userRect.bottom - boundaryRect.top;
        const endX = albRect.left + albRect.width / 2 - boundaryRect.left;
        const endY = albRect.top - boundaryRect.top;
        const length = Math.sqrt(Math.pow(endX - startX, 2) + Math.pow(endY - startY, 2));
        const angle = Math.atan2(endY - startY, endX - startX) * 180 / Math.PI;
        arrow.style.left = startX + 'px';
        arrow.style.top = startY + 'px';
        arrow.style.width = length + 'px';
        arrow.style.transform = `rotate(${angle}deg)`;
        arrow.style.transformOrigin = 'left center';
      }
    }
    
    // ALB to IGW
    const igwBox = document.querySelector('#igw');
    if (albBox && igwBox) {
      const igwRect = igwBox.getBoundingClientRect();
      const arrow = document.querySelector('.arrow-alb-igw');
      if (arrow) {
        const startX = albRect.left + albRect.width / 2 - boundaryRect.left;
        const startY = albRect.top - boundaryRect.top;
        const endY = igwRect.bottom - boundaryRect.top;
        arrow.style.left = startX + 'px';
        arrow.style.top = startY + 'px';
        arrow.style.width = (startY - endY) + 'px';
        arrow.style.transform = 'rotate(90deg)';
        arrow.style.transformOrigin = 'top center';
      }
    }
    
    // ALB to Public Subnets
    const subnet1 = document.querySelector('#public-subnet-1');
    const subnet2 = document.querySelector('#public-subnet-2');
    const subnet3 = document.querySelector('#public-subnet-3');
    if (albBox && subnet1 && subnet2 && subnet3) {
      [subnet1, subnet2, subnet3].forEach((subnet, index) => {
        const subnetRect = subnet.getBoundingClientRect();
        const arrow = document.querySelector(`.arrow-alb-subnet${index + 1}`);
        if (arrow && albBox) {
          const albRect = albBox.getBoundingClientRect();
          const startX = albRect.left + albRect.width / 2 - boundaryRect.left;
          const startY = albRect.bottom - boundaryRect.top;
          const endX = subnetRect.left + subnetRect.width / 2 - boundaryRect.left;
          const endY = subnetRect.top - boundaryRect.top;
          const length = Math.sqrt(Math.pow(endX - startX, 2) + Math.pow(endY - startY, 2));
          const angle = Math.atan2(endY - startY, endX - startX) * 180 / Math.PI;
          arrow.style.left = startX + 'px';
          arrow.style.top = startY + 'px';
          arrow.style.width = length + 'px';
          arrow.style.transform = `rotate(${angle}deg)`;
          arrow.style.transformOrigin = 'left center';
        }
      });
    }
    
    // Public to Private Subnets
    const privateSubnet1 = document.querySelector('#private-subnet-1');
    const privateSubnet2 = document.querySelector('#private-subnet-2');
    const privateSubnet3 = document.querySelector('#private-subnet-3');
    if (subnet1 && privateSubnet1) {
      [privateSubnet1, privateSubnet2, privateSubnet3].forEach((subnet, index) => {
        const publicSubnet = [subnet1, subnet2, subnet3][index];
        const publicRect = publicSubnet.getBoundingClientRect();
        const privateRect = subnet.getBoundingClientRect();
        const arrow = document.querySelector(`.arrow-public-private${index + 1}`);
        if (arrow) {
          const startX = publicRect.left + publicRect.width / 2 - boundaryRect.left;
          const startY = publicRect.bottom - boundaryRect.top;
          const endY = privateRect.top - boundaryRect.top;
          arrow.style.left = startX + 'px';
          arrow.style.top = startY + 'px';
          arrow.style.width = (endY - startY) + 'px';
          arrow.style.transform = 'rotate(90deg)';
          arrow.style.transformOrigin = 'top center';
        }
      });
    }
    
    // Private Subnets to RDS
    const rds1 = document.querySelector('#rds-1');
    const rds2 = document.querySelector('#rds-2');
    const rds3 = document.querySelector('#rds-3');
    if (privateSubnet1 && rds1) {
      [rds1, rds2, rds3].forEach((rds, index) => {
        const privateSubnet = [privateSubnet1, privateSubnet2, privateSubnet3][index];
        const privateRect = privateSubnet.getBoundingClientRect();
        const rdsRect = rds.getBoundingClientRect();
        const arrow = document.querySelector(`.arrow-private-rds${index + 1}`);
        if (arrow) {
          const startX = privateRect.left + privateRect.width / 2 - boundaryRect.left;
          const startY = privateRect.bottom - boundaryRect.top;
          const endY = rdsRect.top - boundaryRect.top;
          arrow.style.left = startX + 'px';
          arrow.style.top = startY + 'px';
          arrow.style.width = (endY - startY) + 'px';
          arrow.style.transform = 'rotate(90deg)';
          arrow.style.transformOrigin = 'top center';
        }
      });
    }
    
    // RDS Failover
    if (rds1 && rds2 && rds3) {
      const rds1Rect = rds1.getBoundingClientRect();
      const rds2Rect = rds2.getBoundingClientRect();
      const rds3Rect = rds3.getBoundingClientRect();
      
      const arrow1 = document.querySelector('.arrow-rds-failover1');
      const arrow2 = document.querySelector('.arrow-rds-failover2');
      
      if (arrow1) {
        const startX = rds1Rect.right - boundaryRect.left;
        const startY = rds2Rect.top + rds2Rect.height / 2 - boundaryRect.top;
        const endX = rds2Rect.left - boundaryRect.left;
        arrow1.style.left = startX + 'px';
        arrow1.style.top = startY + 'px';
        arrow1.style.width = (endX - startX) + 'px';
        arrow1.style.transform = 'rotate(0deg)';
      }
      
      if (arrow2) {
        const startX = rds2Rect.right - boundaryRect.left;
        const startY = rds2Rect.top + rds2Rect.height / 2 - boundaryRect.top;
        const endX = rds3Rect.left - boundaryRect.left;
        arrow2.style.left = startX + 'px';
        arrow2.style.top = startY + 'px';
        arrow2.style.width = (endX - startX) + 'px';
        arrow2.style.transform = 'rotate(0deg)';
      }
    }
  }

  // Position arrows after page load and on resize
  window.addEventListener('load', () => {
    setTimeout(positionArrows, 200);
  });
  
  window.addEventListener('resize', () => {
    setTimeout(positionArrows, 200);
  });

  // Initialize animations with dynamic positioning
  setTimeout(() => {
    positionArrows();
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
