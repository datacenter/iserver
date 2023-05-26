# OpenShift Virtualization - Cat8000v Test Results

```
<?xml version="1.0" ?>
<data xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
	<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
		<version>17.6</version>
		<boot-start-marker/>
		<boot-end-marker/>
		<memory>
			<free>
				<low-watermark>
					<processor>68425</processor>
				</low-watermark>
			</free>
		</memory>
		<call-home>
			<contact-email-addr xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-call-home">sch-smart-licensing@cisco.com</contact-email-addr>
			<tac-profile xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-call-home">
				<profile>
					<CiscoTAC-1>
						<active>true</active>
						<destination>
							<transport-method>http</transport-method>
						</destination>
					</CiscoTAC-1>
				</profile>
			</tac-profile>
		</call-home>
		<service>
			<timestamps>
				<debug-config>
					<datetime>
						<msec/>
					</datetime>
				</debug-config>
				<log-config>
					<datetime>
						<msec/>
					</datetime>
				</log-config>
			</timestamps>
			<call-home/>
		</service>
		<platform>
			<console xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-platform">
				<output>virtual</output>
			</console>
			<qfp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-platform">
				<utilization>
					<monitor>
						<load>80</load>
					</monitor>
				</utilization>
			</qfp>
			<punt-keepalive xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-platform">
				<disable-kernel-core>true</disable-kernel-core>
			</punt-keepalive>
		</platform>
		<hostname>cat8kv-01</hostname>
		<username>
			<name>admin</name>
			<privilege>15</privilege>
			<secret>
				<encryption>9</encryption>
				<secret>$9$5bUzpbrrQoCXwE$LqsARIYgGzzw9yUHff6XF4X2v94PJACIlthl5S6edcw</secret>
			</secret>
		</username>
		<ip>
			<domain>
				<name>cisco.com</name>
			</domain>
			<forward-protocol>
				<protocol>nd</protocol>
			</forward-protocol>
			<ftp>
				<passive/>
			</ftp>
			<multicast>
				<route-limit xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-multicast">2147483647</route-limit>
			</multicast>
			<ssh>
				<version>2</version>
			</ssh>
			<http xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-http">
				<server>false</server>
				<secure-server>true</secure-server>
			</http>
			<igmp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-igmp">
				<snooping>
					<querier/>
				</snooping>
			</igmp>
			<nbar xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-nbar">
				<classification>
					<dns>
						<classify-by-domain/>
					</dns>
				</classification>
			</nbar>
		</ip>
		<interface>
			<GigabitEthernet>
				<name>1</name>
				<switchport>
					<trunk xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-switch">
						<native>
							<vlan-config>
								<tag>true</tag>
							</vlan-config>
						</native>
					</trunk>
				</switchport>
				<ip>
					<address>
						<dhcp/>
					</address>
				</ip>
				<logging>
					<event>
						<link-status/>
					</event>
				</logging>
				<negotiation xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet">
					<auto>true</auto>
				</negotiation>
			</GigabitEthernet>
		</interface>
		<control-plane/>
		<logging>
			<monitor-conf>
				<monitor>false</monitor>
			</monitor-conf>
			<console-conf>
				<console>false</console>
			</console-conf>
		</logging>
		<aaa>
			<new-model xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-aaa"/>
			<authorization xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-aaa">
				<exec>
					<name>default</name>
					<a1>
						<local/>
					</a1>
				</exec>
			</authorization>
			<session-id xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-aaa">common</session-id>
		</aaa>
		<login>
			<on-success>
				<log/>
			</on-success>
		</login>
		<multilink>
			<bundle-name xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ppp">authenticated</bundle-name>
		</multilink>
		<redundancy/>
		<subscriber>
			<templating/>
		</subscriber>
		<ethernet>
			<cfm xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet">
				<alarm>
					<delay>2500</delay>
					<reset>10000</reset>
				</alarm>
			</cfm>
		</ethernet>
		<crypto>
			<pki xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-crypto">
				<certificate>
					<chain>
						<name>SLA-TrustPoint</name>
						<certificate>
							<serial>01</serial>
							<certtype>ca</certtype>
						</certificate>
					</chain>
					<chain>
						<name>TP-self-signed-4246525466</name>
						<certificate>
							<serial>01</serial>
							<certtype>self-signed</certtype>
						</certificate>
					</chain>
				</certificate>
				<trustpoint>
					<id>SLA-TrustPoint</id>
					<enrollment>
						<pkcs12/>
					</enrollment>
					<revocation-check>crl</revocation-check>
				</trustpoint>
				<trustpoint>
					<id>TP-self-signed-4246525466</id>
					<enrollment>
						<selfsigned/>
					</enrollment>
					<revocation-check>none</revocation-check>
					<subject-name>cn=IOS-Self-Signed-Certificate-4246525466</subject-name>
				</trustpoint>
			</pki>
		</crypto>
		<snmp-server>
			<community-config xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-snmp">
				<name>public</name>
				<permission>ro</permission>
			</community-config>
			<community xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-snmp">
				<name>public</name>
				<RO/>
			</community>
			<manager xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-snmp"/>
		</snmp-server>
		<license>
			<udi>
				<pid>C8000V</pid>
				<sn>956JW4WMORD</sn>
			</udi>
		</license>
		<standby>
			<redirects>true</redirects>
		</standby>
		<line>
			<aux>
				<first>0</first>
			</aux>
			<console>
				<first>0</first>
				<length>0</length>
				<stopbits>1</stopbits>
			</console>
			<vty>
				<first>0</first>
				<last>4</last>
				<length>0</length>
				<transport>
					<input>
						<input>ssh</input>
					</input>
				</transport>
			</vty>
		</line>
		<diagnostic xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-diagnostics">
			<bootup>
				<level>minimal</level>
			</bootup>
		</diagnostic>
	</native>
	<netconf-yang xmlns="http://cisco.com/yang/cisco-self-mgmt">
		<cisco-ia xmlns="http://cisco.com/yang/cisco-ia">
			<snmp-trap-control>
				<global-forwarding>true</global-forwarding>
			</snmp-trap-control>
			<snmp-community-string>private</snmp-community-string>
		</cisco-ia>
	</netconf-yang>
	<licensing xmlns="http://cisco.com/ns/yang/cisco-smart-license">
		<config>
			<enable>false</enable>
			<privacy>
				<hostname>false</hostname>
				<version>false</version>
			</privacy>
			<utility>
				<utility-enable>false</utility-enable>
			</utility>
		</config>
	</licensing>
	<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
		<interface>
			<name>GigabitEthernet1</name>
			<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
			<enabled>true</enabled>
			<ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
			<ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
		</interface>
	</interfaces>
	<nacm xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm">
		<enable-nacm>true</enable-nacm>
		<read-default>deny</read-default>
		<write-default>deny</write-default>
		<exec-default>deny</exec-default>
		<enable-external-groups>true</enable-external-groups>
		<rule-list>
			<name>admin</name>
			<group>PRIV15</group>
			<rule>
				<name>permit-all</name>
				<module-name>*</module-name>
				<access-operations>*</access-operations>
				<action>permit</action>
			</rule>
		</rule-list>
	</nacm>
	<routing xmlns="urn:ietf:params:xml:ns:yang:ietf-routing">
		<routing-instance>
			<name>default</name>
			<description>default-vrf [read-only]</description>
			<routing-protocols>
				<routing-protocol>
					<type>static</type>
					<name>1</name>
				</routing-protocol>
			</routing-protocols>
		</routing-instance>
	</routing>
	<interfaces xmlns="http://openconfig.net/yang/interfaces">
		<interface>
			<name>GigabitEthernet1</name>
			<config>
				<name>GigabitEthernet1</name>
				<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
				<enabled>true</enabled>
			</config>
			<subinterfaces>
				<subinterface>
					<index>0</index>
					<config>
						<index>0</index>
						<enabled>true</enabled>
					</config>
					<ipv4 xmlns="http://openconfig.net/yang/interfaces/ip">
						<proxy-arp>
							<config>
								<mode>ALL</mode>
							</config>
						</proxy-arp>
					</ipv4>
					<ipv6 xmlns="http://openconfig.net/yang/interfaces/ip">
						<config>
							<enabled>false</enabled>
						</config>
					</ipv6>
				</subinterface>
			</subinterfaces>
			<ethernet xmlns="http://openconfig.net/yang/interfaces/ethernet">
				<config>
					<mac-address>02:6c:cf:00:00:6a</mac-address>
					<auto-negotiate>true</auto-negotiate>
					<enable-flow-control>true</enable-flow-control>
				</config>
			</ethernet>
		</interface>
	</interfaces>
	<lldp xmlns="http://openconfig.net/yang/lldp">
		<config>
			<enabled>false</enabled>
		</config>
		<interfaces>
			<interface>
				<name>GigabitEthernet1</name>
				<config>
					<name>GigabitEthernet1</name>
					<enabled>true</enabled>
				</config>
			</interface>
		</interfaces>
	</lldp>
	<network-instances xmlns="http://openconfig.net/yang/network-instance">
		<network-instance>
			<name>default</name>
			<config>
				<name>default</name>
				<type xmlns:oc-ni-types="http://openconfig.net/yang/network-instance-types">oc-ni-types:DEFAULT_INSTANCE</type>
				<description>default-vrf [read-only]</description>
			</config>
			<tables>
				<table>
					<protocol xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED</protocol>
					<address-family xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV4</address-family>
					<config>
						<protocol xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED</protocol>
						<address-family xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV4</address-family>
					</config>
				</table>
				<table>
					<protocol xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED</protocol>
					<address-family xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV6</address-family>
					<config>
						<protocol xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED</protocol>
						<address-family xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV6</address-family>
					</config>
				</table>
				<table>
					<protocol xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:STATIC</protocol>
					<address-family xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV4</address-family>
					<config>
						<protocol xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:STATIC</protocol>
						<address-family xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV4</address-family>
					</config>
				</table>
				<table>
					<protocol xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:STATIC</protocol>
					<address-family xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV6</address-family>
					<config>
						<protocol xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:STATIC</protocol>
						<address-family xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV6</address-family>
					</config>
				</table>
			</tables>
			<protocols>
				<protocol>
					<identifier xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:STATIC</identifier>
					<name>DEFAULT</name>
					<config>
						<identifier xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:STATIC</identifier>
						<name>DEFAULT</name>
					</config>
				</protocol>
				<protocol>
					<identifier xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED</identifier>
					<name>DEFAULT</name>
					<config>
						<identifier xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED</identifier>
						<name>DEFAULT</name>
					</config>
				</protocol>
			</protocols>
		</network-instance>
	</network-instances>
</data>
```
