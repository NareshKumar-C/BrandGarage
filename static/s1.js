function saveServiceApplication() {
      const serviceData = {
        name: document.getElementById('name').value,
        carModel: document.getElementById('carModel').value,
        serviceType: document.getElementById('serviceType').value,
        otherService: document.getElementById('otherService').value,
        appointmentDate: document.getElementById('appointmentDate').value,
        contactNumber: document.getElementById('contactNumber').value,
      };
      localStorage.setItem('serviceApplication', JSON.stringify(serviceData));
      alert("Submitted Successfully!");
      window.location.href = "submit.html"; // redirect to confirmation page
    }
function savServiceApplication() {
    document.getElementById("serviceForm").submit();
}

    // Confirmation Page (submit.html) ku use panna
    function loadServiceApplication() {
      const savedData = localStorage.getItem('serviceApplication');
      if (savedData) {
        const serviceData = JSON.parse(savedData);
        document.getElementById('showCarModel').innerText = serviceData.carModel;
        document.getElementById('showServiceType').innerText = serviceData.serviceType;
        document.getElementById('showAppointmentDate').innerText = serviceData.appointmentDate;
        document.getElementById('showContactNumber').innerText = serviceData.contactNumber;
      }
    }