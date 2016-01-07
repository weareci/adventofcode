# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "bento/ubuntu-14.04"
  config.vm.box_check_update = false

  config.vm.provision "chef_apply" do |chef|
    chef.recipe = <<-RECIPE
execute "apt-get update"
%w(python-dev ruby-dev git vim emacs).each do |name|
  package name
end

file "/home/vagrant/.bash_profile" do
  content <<-EOF
if [ -e ~/.bashrc ]; then
  source ~/.bashrc
fi
cd /vagrant
  EOF
end
    RECIPE
  end
end
