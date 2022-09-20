<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="19008000">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="lib" Type="Folder">
			<Item Name="mmW_commands.lvlib" Type="Library" URL="../../../mmw_command_lib/src_LabVIEW/mmW_commands/mmW_commands.lvlib"/>
			<Item Name="mmW_instr_app_API.lvlib" Type="Library" URL="../../../mmw_instr_app_api/mmW_instr_app_API.lvlib"/>
			<Item Name="MsgQ.lvlib" Type="Library" URL="../lib/MsgQ/MsgQ.lvlib"/>
			<Item Name="zmq_multipart_lib.lvlib" Type="Library" URL="../../../zmq_multipart_lib/src_LabVIEW/zmq_mulipart_lib/zmq_multipart_lib.lvlib"/>
		</Item>
		<Item Name="Service.lvlib" Type="Library" URL="../lib/mmw_Service/Service.lvlib"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="instr.lib" Type="Folder">
				<Item Name="5580 BiasBoard power status.ctl" Type="VI" URL="/&lt;instrlib&gt;/niMmWave/ni3620/Config/v1/Host/Public/Typedefs/5580 BiasBoard power status.ctl"/>
				<Item Name="5580 power status.ctl" Type="VI" URL="/&lt;instrlib&gt;/niMmWave/ni3620/Config/v1/Host/Public/Typedefs/5580 power status.ctl"/>
				<Item Name="Adf4002RegMap.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Adf4002RegMap/Adf4002RegMap.lvlib"/>
				<Item Name="Adf5355RegMap.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Adf5355RegMap/Adf5355RegMap.lvlib"/>
				<Item Name="AuxInterfaceRegMap.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/AuxInterfaceRegMap/AuxInterfaceRegMap.lvlib"/>
				<Item Name="BiasControl71RegMap.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/BiasControl71RegMap/BiasControl71RegMap.lvlib"/>
				<Item Name="BiasControl90RegMap.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/BiasControl90RegMap/BiasControl90RegMap.lvlib"/>
				<Item Name="Board Hardware Revision.ctl" Type="VI" URL="/&lt;instrlib&gt;/niMmWave/ni3610 and ni3630/controls/private/Board Hardware Revision.ctl"/>
				<Item Name="Board Information.ctl" Type="VI" URL="/&lt;instrlib&gt;/niMmWave/ni3610 and ni3630/controls/public/Board Information.ctl"/>
				<Item Name="Board Translate HW Revision.vi" Type="VI" URL="/&lt;instrlib&gt;/niMmWave/ni3610 and ni3630/private/Board Translate HW Revision.vi"/>
				<Item Name="BoardControl70RegMap.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/BoardControl70RegMap/BoardControl70RegMap.lvlib"/>
				<Item Name="BoardControlRegMap.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/BoardControlRegMap/BoardControlRegMap.lvlib"/>
				<Item Name="ConnControlRegMap.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/ConnControlRegMap/ConnControlRegMap.lvlib"/>
				<Item Name="Get Base Offset.vi" Type="VI" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Base Offsets/Get Base Offset.vi"/>
				<Item Name="Hmc703RegMap.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Hmc703RegMap/Hmc703RegMap.lvlib"/>
				<Item Name="IfGainRangingRegMap.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/IfGainRangingRegMap/IfGainRangingRegMap.lvlib"/>
				<Item Name="IfInControlRegMap.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/IfInControlRegMap/IfInControlRegMap.lvlib"/>
				<Item Name="IfOutControlRegMap.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/IfOutControlRegMap/IfOutControlRegMap.lvlib"/>
				<Item Name="LO1 Rx Get Base Offset.vi" Type="VI" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Base Offsets/LO1 Rx Get Base Offset.vi"/>
				<Item Name="LO1 Rx Register Maps.ctl" Type="VI" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Base Offsets/LO1 Rx Register Maps.ctl"/>
				<Item Name="LO1 Tx Get Base Offset.vi" Type="VI" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Base Offsets/LO1 Tx Get Base Offset.vi"/>
				<Item Name="LO1 Tx Register Maps.ctl" Type="VI" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Base Offsets/LO1 Tx Register Maps.ctl"/>
				<Item Name="Lo1ControlRegMap.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Lo1ControlRegMap/Lo1ControlRegMap.lvlib"/>
				<Item Name="Lo1IfInSetupRegMap.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Lo1IfInSetupRegMap/Lo1IfInSetupRegMap.lvlib"/>
				<Item Name="Lo1IfOutSetupRegMap.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Lo1IfOutSetupRegMap/Lo1IfOutSetupRegMap.lvlib"/>
				<Item Name="LO2 Get Base Offset.vi" Type="VI" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Base Offsets/LO2 Get Base Offset.vi"/>
				<Item Name="LO2 Register Maps.ctl" Type="VI" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Base Offsets/LO2 Register Maps.ctl"/>
				<Item Name="Lo2ControlRegMap.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Lo2ControlRegMap/Lo2ControlRegMap.lvlib"/>
				<Item Name="Lo2DioSetupRegMap.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Lo2DioSetupRegMap/Lo2DioSetupRegMap.lvlib"/>
				<Item Name="LocalControlRegMap.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/LocalControlRegMap/LocalControlRegMap.lvlib"/>
				<Item Name="Melbourne Get Base Offset.vi" Type="VI" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Base Offsets/Melbourne Get Base Offset.vi"/>
				<Item Name="Melbourne Register Maps.ctl" Type="VI" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Base Offsets/Melbourne Register Maps.ctl"/>
				<Item Name="MelbourneDeckRegMap.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/MelbourneDeckRegMap/MelbourneDeckRegMap.lvlib"/>
				<Item Name="MemInterface70RegMap.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/MemInterface70RegMap/MemInterface70RegMap.lvlib"/>
				<Item Name="Microcontrol70RegMap.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Microcontrol70RegMap/Microcontrol70RegMap.lvlib"/>
				<Item Name="mmWave Digital 70 Get Base Offset.vi" Type="VI" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Base Offsets/mmWave Digital 70 Get Base Offset.vi"/>
				<Item Name="mmWave Digital 70 Register Maps.ctl" Type="VI" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Base Offsets/mmWave Digital 70 Register Maps.ctl"/>
				<Item Name="mmWave Rx Get Base Offset.vi" Type="VI" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Base Offsets/mmWave Rx Get Base Offset.vi"/>
				<Item Name="mmWave Rx Register Maps.ctl" Type="VI" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Base Offsets/mmWave Rx Register Maps.ctl"/>
				<Item Name="mmWave Tx Get Base Offset.vi" Type="VI" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Base Offsets/mmWave Tx Get Base Offset.vi"/>
				<Item Name="mmWave Tx Register Maps.ctl" Type="VI" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Base Offsets/mmWave Tx Register Maps.ctl"/>
				<Item Name="NI 36x2 Get Base Offset.vi" Type="VI" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Base Offsets/NI 36x2 Get Base Offset.vi"/>
				<Item Name="NI 36x2 Register Maps.ctl" Type="VI" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Base Offsets/NI 36x2 Register Maps.ctl"/>
				<Item Name="ni3610_and_ni3630_Driver_Lib.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/ni3610 and ni3630/ni3610_and_ni3630_Driver_Lib.lvlib"/>
				<Item Name="niInstr Basic Elements v1 FPGA.lvlib" Type="Library" URL="/&lt;instrlib&gt;/_niInstr/Basic Elements/v1/FPGA/niInstr Basic Elements v1 FPGA.lvlib"/>
				<Item Name="niInstr Data Formatting v1 FPGA.lvlib" Type="Library" URL="/&lt;instrlib&gt;/_niInstr/Data Formatting/v1/FPGA/niInstr Data Formatting v1 FPGA.lvlib"/>
				<Item Name="niInstr Memory v1 FPGA.lvclass" Type="LVClass" URL="/&lt;instrlib&gt;/_niInstr/Memory/v1/FPGA/Memory/niInstr Memory v1 FPGA.lvclass"/>
				<Item Name="niInstr Register Bus v0 Host.lvlib" Type="Library" URL="/&lt;instrlib&gt;/_niInstr/Register Bus/v0/Host/niInstr Register Bus v0 Host.lvlib"/>
				<Item Name="niMmWave Config v1 Host.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/ni3620/Config/v1/Host/niMmWave Config v1 Host.lvlib"/>
				<Item Name="niMmWave Config v1 Shared.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/ni3620/Config/v1/Shared/niMmWave Config v1 Shared.lvlib"/>
				<Item Name="RefControlRegMap.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/RefControlRegMap/RefControlRegMap.lvlib"/>
				<Item Name="Rx71GHzto76GhzRegMap.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Rx71GHzto76GhzRegMap/Rx71GHzto76GhzRegMap.lvlib"/>
				<Item Name="SMCReadFlash.vi" Type="VI" URL="/&lt;instrlib&gt;/Mulde Driver/private/mm/STC3/SMCReadFlash.vi"/>
				<Item Name="SMCWriteFlash.vi" Type="VI" URL="/&lt;instrlib&gt;/Mulde Driver/private/mm/STC3/SMCWriteFlash.vi"/>
				<Item Name="SynthControlRegMap.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/SynthControlRegMap/SynthControlRegMap.lvlib"/>
				<Item Name="Tx71GHzto76GhzRegMap.lvlib" Type="Library" URL="/&lt;instrlib&gt;/niMmWave/Register Maps/ni3620/v1/Shared/Tx71GHzto76GhzRegMap/Tx71GHzto76GhzRegMap.lvlib"/>
				<Item Name="xsimk0B830B7E81994019B09E50CE7A175B36.dll" Type="Document" URL="/&lt;instrlib&gt;/_niInstr/Basic Elements/v1/FPGA/Private/DFlopBEResetSimFiles/xsim.dir/DFlopBasicElements/xsimk0B830B7E81994019B09E50CE7A175B36.dll"/>
				<Item Name="xsimk6A315D12FBC743E4ACD121A1951E87AC.dll" Type="Document" URL="/&lt;instrlib&gt;/_niInstr/Basic Elements/v1/FPGA/Public/ModGen/ff_max_fanout_8SimFiles/xsim.dir/MaxFanoutFf/xsimk6A315D12FBC743E4ACD121A1951E87AC.dll"/>
				<Item Name="xsimk417FC7712F0F4A3C95450BAF224B3F38.dll" Type="Document" URL="/&lt;instrlib&gt;/_niInstr/Basic Elements/v1/FPGA/Public/ModGen/ff_max_fanout_32SimFiles/xsim.dir/MaxFanoutFf/xsimk417FC7712F0F4A3C95450BAF224B3F38.dll"/>
				<Item Name="xsimk36915C3B0A964A738AD3121E87CF92C2.dll" Type="Document" URL="/&lt;instrlib&gt;/_niInstr/Basic Elements/v1/FPGA/Public/ModGen/ff_max_fanout_16SimFiles/xsim.dir/MaxFanoutFf/xsimk36915C3B0A964A738AD3121E87CF92C2.dll"/>
				<Item Name="xsimkB15BA4892E5F4023A51AA2E61B6FD011.dll" Type="Document" URL="/&lt;instrlib&gt;/_niInstr/Basic Elements/v1/FPGA/Private/GlitchlessMux_4InputSimFiles/xsim.dir/FourInputGlitchFreeMuxBasicElements/xsimkB15BA4892E5F4023A51AA2E61B6FD011.dll"/>
				<Item Name="xsimkC792537791DE412E8810E138F5BC4696.dll" Type="Document" URL="/&lt;instrlib&gt;/_niInstr/Basic Elements/v1/FPGA/Private/DFlopBEPresetSimFiles/xsim.dir/DFlopBasicElements/xsimkC792537791DE412E8810E138F5BC4696.dll"/>
				<Item Name="xsimkE0EDB5E65B8B49DD8E163F5688E824C1.dll" Type="Document" URL="/&lt;instrlib&gt;/_niInstr/Basic Elements/v1/FPGA/Public/ModGen/ff_max_fanout_4SimFiles/xsim.dir/MaxFanoutFf/xsimkE0EDB5E65B8B49DD8E163F5688E824C1.dll"/>
			</Item>
			<Item Name="user.lib" Type="Folder">
				<Item Name="Array of VData to VArray__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Array of VData to VArray__ogtk.vi"/>
				<Item Name="Array of VData to VCluster__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Array of VData to VCluster__ogtk.vi"/>
				<Item Name="Array Size(s)__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Array Size(s)__ogtk.vi"/>
				<Item Name="Array to Array of VData__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Array to Array of VData__ogtk.vi"/>
				<Item Name="Build Error Cluster__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/error/error.llb/Build Error Cluster__ogtk.vi"/>
				<Item Name="Cluster to Array of VData__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Cluster to Array of VData__ogtk.vi"/>
				<Item Name="Encode Section and Key Names__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/variantconfig/variantconfig.llb/Encode Section and Key Names__ogtk.vi"/>
				<Item Name="Get Array Element TD__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Get Array Element TD__ogtk.vi"/>
				<Item Name="Get Array Element TDEnum__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Get Array Element TDEnum__ogtk.vi"/>
				<Item Name="Get Cluster Element Names__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Get Cluster Element Names__ogtk.vi"/>
				<Item Name="Get Cluster Elements TDs__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Get Cluster Elements TDs__ogtk.vi"/>
				<Item Name="Get Data Name from TD__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Get Data Name from TD__ogtk.vi"/>
				<Item Name="Get Data Name__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Get Data Name__ogtk.vi"/>
				<Item Name="Get Default Data from TD__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Get Default Data from TD__ogtk.vi"/>
				<Item Name="Get Element TD from Array TD__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Get Element TD from Array TD__ogtk.vi"/>
				<Item Name="Get Header from TD__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Get Header from TD__ogtk.vi"/>
				<Item Name="Get Last PString__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Get Last PString__ogtk.vi"/>
				<Item Name="Get PString__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Get PString__ogtk.vi"/>
				<Item Name="Get Strings from Enum TD__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Get Strings from Enum TD__ogtk.vi"/>
				<Item Name="Get Strings from Enum__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Get Strings from Enum__ogtk.vi"/>
				<Item Name="Get TDEnum from Data__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Get TDEnum from Data__ogtk.vi"/>
				<Item Name="Get Variant Attributes__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Get Variant Attributes__ogtk.vi"/>
				<Item Name="Get Waveform Type Enum from TD__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Get Waveform Type Enum from TD__ogtk.vi"/>
				<Item Name="Parse String with TDs__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Parse String with TDs__ogtk.vi"/>
				<Item Name="Read INI Cluster__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/variantconfig/variantconfig.llb/Read INI Cluster__ogtk.vi"/>
				<Item Name="Read Key (Variant)__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/variantconfig/variantconfig.llb/Read Key (Variant)__ogtk.vi"/>
				<Item Name="Read Section Cluster__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/variantconfig/variantconfig.llb/Read Section Cluster__ogtk.vi"/>
				<Item Name="Reshape 1D Array__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Reshape 1D Array__ogtk.vi"/>
				<Item Name="Reshape Array to 1D VArray__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Reshape Array to 1D VArray__ogtk.vi"/>
				<Item Name="Set Cluster Element by Name__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Set Cluster Element by Name__ogtk.vi"/>
				<Item Name="Set Data Name__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Set Data Name__ogtk.vi"/>
				<Item Name="Set Enum String Value__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Set Enum String Value__ogtk.vi"/>
				<Item Name="Split Cluster TD__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Split Cluster TD__ogtk.vi"/>
				<Item Name="Strip Units__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Strip Units__ogtk.vi"/>
				<Item Name="Trim Whitespace (String Array)__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/string/string.llb/Trim Whitespace (String Array)__ogtk.vi"/>
				<Item Name="Trim Whitespace (String)__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/string/string.llb/Trim Whitespace (String)__ogtk.vi"/>
				<Item Name="Trim Whitespace__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/string/string.llb/Trim Whitespace__ogtk.vi"/>
				<Item Name="Type Descriptor Enumeration__ogtk.ctl" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Type Descriptor Enumeration__ogtk.ctl"/>
				<Item Name="Type Descriptor Header__ogtk.ctl" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Type Descriptor Header__ogtk.ctl"/>
				<Item Name="Type Descriptor__ogtk.ctl" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Type Descriptor__ogtk.ctl"/>
				<Item Name="Variant to Header Info__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Variant to Header Info__ogtk.vi"/>
				<Item Name="Waveform Subtype Enum__ogtk.ctl" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/lvdata/lvdata.llb/Waveform Subtype Enum__ogtk.ctl"/>
			</Item>
			<Item Name="vi.lib" Type="Folder">
				<Item Name="8.6CompatibleGlobalVar.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/config.llb/8.6CompatibleGlobalVar.vi"/>
				<Item Name="adapter data.ctl" Type="VI" URL="/&lt;vilib&gt;/LabVIEW Targets/FPGA/niMmWave/ni3620/adapter data.ctl"/>
				<Item Name="Application Directory.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Application Directory.vi"/>
				<Item Name="BuildHelpPath.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/BuildHelpPath.vi"/>
				<Item Name="Check if File or Folder Exists.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Check if File or Folder Exists.vi"/>
				<Item Name="Check Special Tags.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Check Special Tags.vi"/>
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="Close Registry Key.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Close Registry Key.vi"/>
				<Item Name="Convert property node font to graphics font.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Convert property node font to graphics font.vi"/>
				<Item Name="Details Display Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Details Display Dialog.vi"/>
				<Item Name="DialogType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogType.ctl"/>
				<Item Name="DialogTypeEnum.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogTypeEnum.ctl"/>
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="Error Code Database.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Code Database.vi"/>
				<Item Name="ErrWarn.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/ErrWarn.ctl"/>
				<Item Name="eventvkey.ctl" Type="VI" URL="/&lt;vilib&gt;/event_ctls.llb/eventvkey.ctl"/>
				<Item Name="Field_RnD_Services_Logger_Toolkit.lvlib" Type="Library" URL="/&lt;vilib&gt;/Field R&amp;D Services/Logger/Field_RnD_Services_Logger_Toolkit.lvlib"/>
				<Item Name="Find Tag.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find Tag.vi"/>
				<Item Name="Format Message String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Format Message String.vi"/>
				<Item Name="FormatTime String.vi" Type="VI" URL="/&lt;vilib&gt;/express/express execution control/ElapsedTimeBlock.llb/FormatTime String.vi"/>
				<Item Name="G#Object.lvclass" Type="LVClass" URL="/&lt;vilib&gt;/addons/_AddQ/G#Object/G#Object.lvclass"/>
				<Item Name="General Error Handler Core CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler Core CORE.vi"/>
				<Item Name="General Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler.vi"/>
				<Item Name="Get LV Class Default Value.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/LVClass/Get LV Class Default Value.vi"/>
				<Item Name="Get LV Class Path.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/LVClass/Get LV Class Path.vi"/>
				<Item Name="Get String Text Bounds.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Get String Text Bounds.vi"/>
				<Item Name="Get System Directory.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/sysdir.llb/Get System Directory.vi"/>
				<Item Name="Get Text Rect.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Get Text Rect.vi"/>
				<Item Name="GetHelpDir.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetHelpDir.vi"/>
				<Item Name="getNi3620RioInterfaceNumberFromFpgaRef.vi" Type="VI" URL="/&lt;vilib&gt;/LabVIEW Targets/FPGA/niMmWave/ni3620/getNi3620RioInterfaceNumberFromFpgaRef.vi"/>
				<Item Name="GetRTHostConnectedProp.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetRTHostConnectedProp.vi"/>
				<Item Name="High Resolution Relative Seconds.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/High Resolution Relative Seconds.vi"/>
				<Item Name="JKI JSON Serialization.lvlib" Type="Library" URL="/&lt;vilib&gt;/addons/_JKI.lib/Serialization/JSON/JKI JSON Serialization.lvlib"/>
				<Item Name="JKI Serialization.lvlib" Type="Library" URL="/&lt;vilib&gt;/addons/_JKI.lib/Serialization/Core/JKI Serialization.lvlib"/>
				<Item Name="JKI Unicode.lvlib" Type="Library" URL="/&lt;vilib&gt;/addons/_JKI.lib/Unicode/JKI Unicode.lvlib"/>
				<Item Name="Longest Line Length in Pixels.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Longest Line Length in Pixels.vi"/>
				<Item Name="LVBoundsTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVBoundsTypeDef.ctl"/>
				<Item Name="LVDateTimeRec.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVDateTimeRec.ctl"/>
				<Item Name="LVRectTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVRectTypeDef.ctl"/>
				<Item Name="lvSimController.dll" Type="Document" URL="/&lt;vilib&gt;/rvi/Simulation/lvSimController.dll"/>
				<Item Name="ni3620_close.vi" Type="VI" URL="/&lt;vilib&gt;/LabVIEW Targets/FPGA/niMmWave/ni3620/ni3620_close.vi"/>
				<Item Name="ni3620_open.vi" Type="VI" URL="/&lt;vilib&gt;/LabVIEW Targets/FPGA/niMmWave/ni3620/ni3620_open.vi"/>
				<Item Name="ni3620_read.vi" Type="VI" URL="/&lt;vilib&gt;/LabVIEW Targets/FPGA/niMmWave/ni3620/ni3620_read.vi"/>
				<Item Name="ni3620_write.vi" Type="VI" URL="/&lt;vilib&gt;/LabVIEW Targets/FPGA/niMmWave/ni3620/ni3620_write.vi"/>
				<Item Name="NI_AALBase.lvlib" Type="Library" URL="/&lt;vilib&gt;/Analysis/NI_AALBase.lvlib"/>
				<Item Name="NI_AALPro.lvlib" Type="Library" URL="/&lt;vilib&gt;/Analysis/NI_AALPro.lvlib"/>
				<Item Name="NI_Data Type.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/Data Type/NI_Data Type.lvlib"/>
				<Item Name="NI_FileType.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/lvfile.llb/NI_FileType.lvlib"/>
				<Item Name="NI_Gmath.lvlib" Type="Library" URL="/&lt;vilib&gt;/gmath/NI_Gmath.lvlib"/>
				<Item Name="NI_LVConfig.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/config.llb/NI_LVConfig.lvlib"/>
				<Item Name="NI_MABase.lvlib" Type="Library" URL="/&lt;vilib&gt;/measure/NI_MABase.lvlib"/>
				<Item Name="NI_MAPro.lvlib" Type="Library" URL="/&lt;vilib&gt;/measure/NI_MAPro.lvlib"/>
				<Item Name="NI_Matrix.lvlib" Type="Library" URL="/&lt;vilib&gt;/Analysis/Matrix/NI_Matrix.lvlib"/>
				<Item Name="NI_PackedLibraryUtility.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/LVLibp/NI_PackedLibraryUtility.lvlib"/>
				<Item Name="nisyscfg.lvlib" Type="Library" URL="/&lt;vilib&gt;/nisyscfg/nisyscfg.lvlib"/>
				<Item Name="Not Found Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Not Found Dialog.vi"/>
				<Item Name="Number of Waveform Samples.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/WDTOps.llb/Number of Waveform Samples.vi"/>
				<Item Name="Open Registry Key.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Open Registry Key.vi"/>
				<Item Name="Qualified Name Array To Single String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/LVClass/Qualified Name Array To Single String.vi"/>
				<Item Name="Read Registry Value DWORD.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value DWORD.vi"/>
				<Item Name="Read Registry Value Simple STR.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value Simple STR.vi"/>
				<Item Name="Read Registry Value Simple U32.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value Simple U32.vi"/>
				<Item Name="Read Registry Value Simple.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value Simple.vi"/>
				<Item Name="Read Registry Value STR.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value STR.vi"/>
				<Item Name="Read Registry Value.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value.vi"/>
				<Item Name="Registry Handle Master.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry Handle Master.vi"/>
				<Item Name="Registry refnum.ctl" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry refnum.ctl"/>
				<Item Name="Registry RtKey.ctl" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry RtKey.ctl"/>
				<Item Name="Registry SAM.ctl" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry SAM.ctl"/>
				<Item Name="Registry Simplify Data Type.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry Simplify Data Type.vi"/>
				<Item Name="Registry View.ctl" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry View.ctl"/>
				<Item Name="Registry WinErr-LVErr.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry WinErr-LVErr.vi"/>
				<Item Name="Search and Replace Pattern.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Search and Replace Pattern.vi"/>
				<Item Name="Set Bold Text.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set Bold Text.vi"/>
				<Item Name="Set String Value.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set String Value.vi"/>
				<Item Name="Simple Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Simple Error Handler.vi"/>
				<Item Name="Space Constant.vi" Type="VI" URL="/&lt;vilib&gt;/dlg_ctls.llb/Space Constant.vi"/>
				<Item Name="Stall Data Flow.vim" Type="VI" URL="/&lt;vilib&gt;/Utility/Stall Data Flow.vim"/>
				<Item Name="STR_ASCII-Unicode.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/STR_ASCII-Unicode.vi"/>
				<Item Name="subElapsedTime.vi" Type="VI" URL="/&lt;vilib&gt;/express/express execution control/ElapsedTimeBlock.llb/subElapsedTime.vi"/>
				<Item Name="subTimeDelay.vi" Type="VI" URL="/&lt;vilib&gt;/express/express execution control/TimeDelayBlock.llb/subTimeDelay.vi"/>
				<Item Name="System Directory Type.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/sysdir.llb/System Directory Type.ctl"/>
				<Item Name="System Exec.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/system.llb/System Exec.vi"/>
				<Item Name="TagReturnType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/TagReturnType.ctl"/>
				<Item Name="Three Button Dialog CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog CORE.vi"/>
				<Item Name="Three Button Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog.vi"/>
				<Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
				<Item Name="VariantType.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/VariantDataType/VariantType.lvlib"/>
				<Item Name="VISA Register Access Address Space.ctl" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Register Access Address Space.ctl"/>
				<Item Name="VISA Unmap Trigger Trigger Source.ctl" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Unmap Trigger Trigger Source.ctl"/>
				<Item Name="WDT Number of Waveform Samples CDB.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/WDTOps.llb/WDT Number of Waveform Samples CDB.vi"/>
				<Item Name="WDT Number of Waveform Samples DBL.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/WDTOps.llb/WDT Number of Waveform Samples DBL.vi"/>
				<Item Name="WDT Number of Waveform Samples EXT.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/WDTOps.llb/WDT Number of Waveform Samples EXT.vi"/>
				<Item Name="WDT Number of Waveform Samples I8.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/WDTOps.llb/WDT Number of Waveform Samples I8.vi"/>
				<Item Name="WDT Number of Waveform Samples I16.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/WDTOps.llb/WDT Number of Waveform Samples I16.vi"/>
				<Item Name="WDT Number of Waveform Samples I32.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/WDTOps.llb/WDT Number of Waveform Samples I32.vi"/>
				<Item Name="WDT Number of Waveform Samples SGL.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/WDTOps.llb/WDT Number of Waveform Samples SGL.vi"/>
				<Item Name="whitespace.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/whitespace.ctl"/>
				<Item Name="zeromq.lvlib" Type="Library" URL="/&lt;vilib&gt;/addons/zeromq/zeromq.lvlib"/>
			</Item>
			<Item Name="ADC Sync Injection.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Calibration/ADC Sync Injection.vi"/>
			<Item Name="Advapi32.dll" Type="Document" URL="Advapi32.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="Align TClk.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Sync/Align TClk.vi"/>
			<Item Name="Baseband Resources.ctl" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/TypeDefs/Baseband Resources.ctl"/>
			<Item Name="Blank FPGA Reference.ctl" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/TypeDefs/Blank FPGA Reference.ctl"/>
			<Item Name="Calculate Channel Skew.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Calibration/Calculate Channel Skew.vi"/>
			<Item Name="Calculate Eq Measurements.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Calibration/Calculate Eq Measurements.vi"/>
			<Item Name="Calculate Image.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Calibration/Calculate Image.vi"/>
			<Item Name="Calculate Mapping.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Calibration/Calculate Mapping.vi"/>
			<Item Name="Calculate Sample Delay.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Sync/Calculate Sample Delay.vi"/>
			<Item Name="Calculate Single Point Correction.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Calibration/Calculate Single Point Correction.vi"/>
			<Item Name="Calculate Spectrum.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Utility/Calculate Spectrum.vi"/>
			<Item Name="Calibrate and Sync.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Calibration/Calibrate and Sync.vi"/>
			<Item Name="Calibrate TDC.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Sync/Calibrate TDC.vi"/>
			<Item Name="Channel Configuration.ctl" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/TypeDefs/Channel Configuration.ctl"/>
			<Item Name="Check ADC status.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Utility/Check ADC status.vi"/>
			<Item Name="Check alarms.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Utility/Check alarms.vi"/>
			<Item Name="Check Multichassis Sync Support.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Utility/Check Multichassis Sync Support.vi"/>
			<Item Name="CommandResponse communication.lvlib" Type="Library" URL="../../../mmw_instrument/src_LabVIEW/Host/Intertarget communication/CommandResponse communication.lvlib"/>
			<Item Name="Configure Chevelle JESD Rx.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Configure/Configure Chevelle JESD Rx.vi"/>
			<Item Name="Configure Chevelle JESD TX.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Configure/Configure Chevelle JESD TX.vi"/>
			<Item Name="Configure IQ Inversion.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Calibration/Configure IQ Inversion.vi"/>
			<Item Name="Constants.ctl" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/TypeDefs/Constants.ctl"/>
			<Item Name="Detected mmWave Adapters.ctl" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/TypeDefs/Detected mmWave Adapters.ctl"/>
			<Item Name="Direction.ctl" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/TypeDefs/Direction.ctl"/>
			<Item Name="Enable Reference Output.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Configure/Enable Reference Output.vi"/>
			<Item Name="Forward BP Trigger.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Configure/Forward BP Trigger.vi"/>
			<Item Name="FPGA Utility.lvlib" Type="Library" URL="../../../mmw_instrument/src_LabVIEW/FPGA/SubVIs/Utility/FPGA Utility.lvlib"/>
			<Item Name="Fractional Delay Coefficients.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Calibration/Fractional Delay Coefficients.vi"/>
			<Item Name="Front End Configuration.ctl" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/TypeDefs/Front End Configuration.ctl"/>
			<Item Name="Gain Ranging.ctl" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/TypeDefs/Gain Ranging.ctl"/>
			<Item Name="Get Constants.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Utility/Get Constants.vi"/>
			<Item Name="Get Rx Tx resources.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Get Rx Tx resources.vi"/>
			<Item Name="Global Constants.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Utility/Global Constants.vi"/>
			<Item Name="Hardware Configuration.ctl" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/TypeDefs/Hardware Configuration.ctl"/>
			<Item Name="Hardware Settings.ctl" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Calibration/Hardware Settings.ctl"/>
			<Item Name="Initialize Constants.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Utility/Initialize Constants.vi"/>
			<Item Name="IQ Impairments impl.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Utility/IQ Impairments impl.vi"/>
			<Item Name="JESD Sync TX.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Configure/JESD Sync TX.vi"/>
			<Item Name="kernel32.dll" Type="Document" URL="kernel32.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="lvanlys.dll" Type="Document" URL="/&lt;resource&gt;/lvanlys.dll"/>
			<Item Name="Measure Skew.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Sync/Measure Skew.vi"/>
			<Item Name="Measure TClk Skew.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Sync/Measure TClk Skew.vi"/>
			<Item Name="Measure TDC.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Sync/Measure TDC.vi"/>
			<Item Name="Measure Time Skew.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Calibration/Measure Time Skew.vi"/>
			<Item Name="Measure.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Calibration/Measure.vi"/>
			<Item Name="Measurements.ctl" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Calibration/Measurements.ctl"/>
			<Item Name="mmWave Adapter Information.ctl" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/TypeDefs/mmWave Adapter Information.ctl"/>
			<Item Name="mmWave data.lvclass" Type="LVClass" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/mmWave data_class/mmWave data.lvclass"/>
			<Item Name="mmWave HW Control.lvlib" Type="Library" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/mmWave HW Control/mmWave HW Control.lvlib"/>
			<Item Name="mmWave instrument.lvclass" Type="LVClass" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/mmWave instrument_class/mmWave instrument.lvclass"/>
			<Item Name="NiFpgaLv.dll" Type="Document" URL="NiFpgaLv.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="niMMSupportu.dll" Type="Document" URL="niMMSupportu.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="nirioOpera.dll" Type="Document" URL="nirioOpera.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="nisyscfg.dll" Type="Document" URL="nisyscfg.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="Open Cal Acq.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Calibration/Open Cal Acq.vi"/>
			<Item Name="Parse Alarm Error.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Utility/Parse Alarm Error.vi"/>
			<Item Name="Parse Option String.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Utility/Parse Option String.vi"/>
			<Item Name="Populate PXI Trigger Bus Information.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Utility/Populate PXI Trigger Bus Information.vi"/>
			<Item Name="PXI Trigger Bus Info.ctl" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/TypeDefs/PXI Trigger Bus Info.ctl"/>
			<Item Name="Read Cal Acq Data.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Calibration/Read Cal Acq Data.vi"/>
			<Item Name="Read TDC Measusrement.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Sync/Read TDC Measusrement.vi"/>
			<Item Name="Remove Time Skew.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Calibration/Remove Time Skew.vi"/>
			<Item Name="Reorder Coefficients.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Utility/Reorder Coefficients.vi"/>
			<Item Name="Reset TDC.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Sync/Reset TDC.vi"/>
			<Item Name="Resources.ctl" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/TypeDefs/Resources.ctl"/>
			<Item Name="Route Triggers Impl.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Configure/Route Triggers Impl.vi"/>
			<Item Name="Route Triggers.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Configure/Route Triggers.vi"/>
			<Item Name="Rx Baseband Session.ctl" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/TypeDefs/Rx Baseband Session.ctl"/>
			<Item Name="RX Close.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Configure/RX Close.vi"/>
			<Item Name="RX Detect Sync Error.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Configure/RX Detect Sync Error.vi"/>
			<Item Name="RX driver FPGA ref.ctl" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/TypeDefs/RX driver FPGA ref.ctl"/>
			<Item Name="RX FPGA Reference.ctl" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/TypeDefs/RX FPGA Reference.ctl"/>
			<Item Name="RX JESD Sync.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Configure/RX JESD Sync.vi"/>
			<Item Name="RX Multi Module Sync.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Sync/RX Multi Module Sync.vi"/>
			<Item Name="RX TX Open (N Channel).vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/RX TX Open (N Channel).vi"/>
			<Item Name="RX_FPGA_driver_DRAM_v1_2.lvbitx" Type="Document" URL="../../../mmw_instrument/src_LabVIEW/FPGA Bitfiles/RX_FPGA_driver_DRAM_v1_2.lvbitx"/>
			<Item Name="Session.ctl" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/TypeDefs/Session.ctl"/>
			<Item Name="Set 20 kHz TClk Parameters.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Configure/Set 20 kHz TClk Parameters.vi"/>
			<Item Name="Set Alignment Complete.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Sync/Set Alignment Complete.vi"/>
			<Item Name="Set Delay.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Sync/Set Delay.vi"/>
			<Item Name="Set Fractional Delay.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Calibration/Set Fractional Delay.vi"/>
			<Item Name="Set TClk Offset.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Sync/Set TClk Offset.vi"/>
			<Item Name="Set TClk Parameters.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Sync/Set TClk Parameters.vi"/>
			<Item Name="Shared FPGA Reference.ctl" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/TypeDefs/Shared FPGA Reference.ctl"/>
			<Item Name="Shared.lvlib" Type="Library" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Shared/Shared.lvlib"/>
			<Item Name="Sync DAC LMK04832.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Configure/Sync DAC LMK04832.vi"/>
			<Item Name="Sync SysRef.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Configure/Sync SysRef.vi"/>
			<Item Name="Sync TX.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Sync/Sync TX.vi"/>
			<Item Name="Tclk Parameters.ctl" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Sync/Tclk Parameters.ctl"/>
			<Item Name="tdc calibration data.ctl" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Sync/tdc calibration data.ctl"/>
			<Item Name="TimeBenchmark.lvlib" Type="Library" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/TimeBenchmark/TimeBenchmark.lvlib"/>
			<Item Name="Trigger Control.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Sync/Trigger Control.vi"/>
			<Item Name="Tx Baseband Session.ctl" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/TypeDefs/Tx Baseband Session.ctl"/>
			<Item Name="TX Close.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Configure/TX Close.vi"/>
			<Item Name="TX driver FPGA ref.ctl" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/TypeDefs/TX driver FPGA ref.ctl"/>
			<Item Name="TX FPGA Reference.ctl" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/TypeDefs/TX FPGA Reference.ctl"/>
			<Item Name="TX trigger config.ctl" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/TypeDefs/TX trigger config.ctl"/>
			<Item Name="TX_FPGA_driver_DRAM_v1_2_1.lvbitx" Type="Document" URL="../../../mmw_instrument/src_LabVIEW/FPGA Bitfiles/TX_FPGA_driver_DRAM_v1_2_1.lvbitx"/>
			<Item Name="Verify Matching Board Capabilities.vi" Type="VI" URL="../../../mmw_instrument/src_LabVIEW/Host/SubVIs/Low-level/Configure/Verify Matching Board Capabilities.vi"/>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="mmWave Service" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{1EDAC39A-576F-4BF4-89A6-1DBAA66FB169}</Property>
				<Property Name="App_INI_GUID" Type="Str">{FA3F0103-C838-4BCF-BE0F-BB5B88C42E0D}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{1B0F1B50-D88A-4914-9F98-68A45214FC4F}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">mmWave Service</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/NI_AB_PROJECTNAME/mmWave Service</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{303B7437-8C1C-4A4F-BC3C-AC17701807FE}</Property>
				<Property Name="Bld_version.build" Type="Int">2</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">mmWave_Service.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/NI_AB_PROJECTNAME/mmWave Service/mmWave_Service.exe</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/NI_AB_PROJECTNAME/mmWave Service/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{42449209-5750-44AF-AA7A-0018208C5AF6}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/Service.lvlib/Service.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="Source[2].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[2].itemID" Type="Ref">/My Computer/Service.lvlib/DLLs/libzmq32.dll</Property>
				<Property Name="Source[2].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[3].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[3].itemID" Type="Ref">/My Computer/Service.lvlib/DLLs/libzmq64.dll</Property>
				<Property Name="Source[3].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[4].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[4].itemID" Type="Ref">/My Computer/Service.lvlib/DLLs/lvzmq32.dll</Property>
				<Property Name="Source[4].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[5].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[5].itemID" Type="Ref">/My Computer/Service.lvlib/DLLs/lvzmq64.dll</Property>
				<Property Name="Source[5].sourceInclusion" Type="Str">Include</Property>
				<Property Name="SourceCount" Type="Int">6</Property>
				<Property Name="TgtF_companyName" Type="Str">Forsteh d.o.o</Property>
				<Property Name="TgtF_fileDescription" Type="Str">mmWave Service</Property>
				<Property Name="TgtF_internalName" Type="Str">mmWave Service</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2020 Forsteh d.o.o</Property>
				<Property Name="TgtF_productName" Type="Str">mmWave Service</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{6B078442-8DBA-4FBA-83A5-690FAB67D673}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">mmWave_Service.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
		</Item>
	</Item>
</Project>
