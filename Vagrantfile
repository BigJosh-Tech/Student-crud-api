# Vagrantfile
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"
  config.vm.network "forwarded_port", guest: 8080, host: 8080

  # Sync folders (optional, adjust to your needs)
  config.vm.synced_folder ".", "/home/vagrant/student-api", type: "virtualbox"

  config.vm.provision "shell", path: "provision.sh"

  # Disable automatic vbguest updates (optional for stability)
  if Vagrant.has_plugin?("vagrant-vbguest")
    config.vbguest.auto_update = false
  end
  

  # VirtualBox specific settings
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
    vb.cpus = 2
  end
end
